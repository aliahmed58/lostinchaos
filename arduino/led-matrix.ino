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

void setup() {
  set_pin_modes();
  init_led_strips();
  clear_screen();

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

}
