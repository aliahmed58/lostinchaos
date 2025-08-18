#define CLOCK_PIN 2
// width of total screen i.e. 24 leds in 3 strips
#define W 24
// height of total screen i.e. 32 leds in 3 strips
#define H 32

#define MATRIX_COUNT (H / 8)
// no. of strips
#define NO_OF_STRIPS 3
// data pins from left most strip to right most strip
int dataPins[NO_OF_STRIPS] = {8, 6, 4};
// latch pins from left most strip to right most strip
int latchPins[NO_OF_STRIPS] = {7, 5, 3};

// LED matrix settings go here
#define INTENSITY 0x00 // lowest intensity of led lights

// letters of my name major col order :P
unsigned char a[4] = {
        0b1111,
        0b1010,
        0b1010,
        0b1111
};

unsigned char l[4] = {
    0b1111,
    0b1111,
    0b0001,
    0b0001
};

unsigned char i[4] = {
  0b1001,
  0b1111,
  0b1111,
  0b1001
};

unsigned char buffer[24 * 32] = {0};

// set pin modes of arduino pins im using
void set_pin_modes() {
  for (int i = 0; i < NO_OF_STRIPS; i ++) {
    pinMode(dataPins[i], OUTPUT);
    pinMode(latchPins[i], OUTPUT);
  }
  pinMode(CLOCK_PIN, OUTPUT);
}


// initial setup for led matrices
void init_led_strips() {
  for (int i = 0; i < NO_OF_STRIPS; i++) {
    writeAll(dataPins[i], latchPins[i], 0x0c, 0x01);
    writeAll(dataPins[i], latchPins[i], 0x09, 0x00); // no decode mode
    writeAll(dataPins[i], latchPins[i], 0x0A, INTENSITY); // light intensity
    writeAll(dataPins[i], latchPins[i], 0x0B, 0x07); // scan limit to all 7
    writeAll(dataPins[i], latchPins[i], 0x0f, 0x00); // shutdown mode off
  }
}

// display test for strip
void display_test(int strip_no) {
  writeAll(dataPins[strip_no], latchPins[strip_no], 0x0A, 0x00);
  delay(100);
}

void clear(int dataPin, int latchPin) {
  // write 0b00000000 to all columns
  for (byte col = 1; col <= 8; col ++) {
    writeAll(dataPin, latchPin, col, 0x00);
  }
}

// --------------------------------------------------------------
// functions below manipulate :( all 3 led strips as a single screen
// --------------------------------------------------------------

// clear screen
void clear_screen() {
  for (int i = 0; i < NO_OF_STRIPS; i ++) {
    clear(dataPins[i], latchPins[i]);
  }
}

// draw a rect from x,y to x + w, y + h
void draw_rect(int x, int y, int w, int h) {
  if (!validate_xy(x, y) || !validate_xy(x + w, y + h)) {
    return;
  }

  for (int c = x; c < x + w; c ++) {
    for (int r = y; r < y + h; r ++) {
      buffer[W * r + c] = 1;
    }
  }
}

void draw_letter(int x, int y, unsigned char letter[]) {
  if (!validate_xy(x, y) || !validate_xy(x + 4, y + 4)) {
    return;
  }

  for (int c = 0; c < 4; c ++) {
    for (int r = 0; r < 4; r ++) {
      if (letter[c] & (0b1000 >> r)) {
        buffer[W * (r + y) + (c + x)] = 1;
      }
    }
  }
}

unsigned char matrix_data[MATRIX_COUNT] = {0};

void render() {
  for (int col = 0; col < W; col ++) {
    int strip = col / 8;
    for (int row = 0; row < H; row ++) {
      if (buffer[W * row + col] == 0) {
        continue;
      }
      int matrix = row / 8;
      int matrix_cell = row % 8;
      matrix_data[matrix] |= (int) ceil(pow(2, (7 - matrix_cell)));
      // written to matrix, no need of that value now, clear buffer
      buffer[W * row + col] = 0;
    }

    for (int i = 0; i < MATRIX_COUNT; i ++) {
      writeToNthMatrix(dataPins[strip], latchPins[strip], i, 8 - (col % 8), matrix_data[i]);
      matrix_data[i] = 0;
    }
  }

}

bool validate_xy(int x, int y) {
  return x >= 0 && x < W && y >= 0 && y < H;
}

void writeAll(int dataPin, int latchPin, int d1, int d2) {
  digitalWrite(latchPin, LOW);
  for (int i = 0; i < 4; i ++) {
    shiftOut(dataPin, CLOCK_PIN, MSBFIRST, d1);
    shiftOut(dataPin, CLOCK_PIN, MSBFIRST, d2);
  }
  digitalWrite(latchPin, HIGH);
}

void writeOne(int dataPin, int latchPin, int d1, int d2) {
  digitalWrite(latchPin, LOW);
  shiftOut(dataPin, CLOCK_PIN, MSBFIRST, d1);
  shiftOut(dataPin, CLOCK_PIN, MSBFIRST, d2);
  digitalWrite(latchPin, HIGH);
}

int x = 0;
int y = 30;

// HAVE TO SORT OUT MESSY CODE
void setup() {
  set_pin_modes();
  init_led_strips();
  clear_screen();
  // draw_rect(0, 4, 2, 10);
  // draw_rect(2, 4, 1, 2);
  // draw_rect(2, 9, 1, 2);
  // draw_rect(3, 4, 2, 10);
  // if something coms up on the same row twice like
  draw_letter(0, 0, a);
  draw_letter(5, 0, l);
  draw_letter(10, 0, i);

  render();
  // the above 2 commands are not gonna work, because it multiplexes once in a row
  // so anything that's being drawn, need to see if it's gonna be in a single row, and append it.
  // should probably use a W * H array and update that with 1s and then draw that, so it's easier.
  // draw_rect(6, 4, 2, 10);
  // draw_rect(6, 4, 2, 10);
  // draw_rect(8, 12, 4, 2);

  // draw_rect(13, 4, 2, 10);
  // writeToNthMatrix(dataPins[0], latchPins[0], 1, 0, 0);
  // writeToNthMatrix(dataPins[0], latchPins[0], 2, 1, 0b11110011);
  // draw_rect(0, 0, 1, 1);
}

void writeToNthMatrix(int dataPin, int latchPin, int m, byte d1, byte d2) {
    digitalWrite(latchPin, LOW);
    for (int i = 0; i < 4; i++) {
    if (i == m) {
      shiftOut(dataPin, CLOCK_PIN, MSBFIRST, d1);   // Register
      shiftOut(dataPin, CLOCK_PIN, MSBFIRST, d2);  // Data
    } else {
      shiftOut(dataPin, CLOCK_PIN, MSBFIRST, 0); // No-op
      shiftOut(dataPin, CLOCK_PIN, MSBFIRST, 0);
    }
  }
    digitalWrite(latchPin, HIGH);

}

void loop() {

  draw_rect(5, y, 1, 1);
  draw_rect(10, y, 1, 1);
  render();
  y -= 3;
  if (y < 0) {
    y = 30;
  }

}
