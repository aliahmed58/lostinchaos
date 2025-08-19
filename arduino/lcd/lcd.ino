int rs = 9;   // H: data, L: instruction code
int e = 10;    // H,H -> L chip enable signal
int out = 11;  // data pin to 8 bit shift reg
int rclk = 12;
int srclk = 13;

// voltage resistors to rmr
// R2 = 220Ohm
// R1 = 680Ohm on Vin 5v

int cursor = 0x00;

void setup() {
  pinMode(rs, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(out, OUTPUT);
  pinMode(rclk, OUTPUT);
  pinMode(srclk, OUTPUT);
  init_mode();
  set_display();
  write_instruction(0b00000110);
  clear_display();
  shiftOut(out, srclk, LSBFIRST, 0);
  digitalWrite(rclk, LOW);
  digitalWrite(rclk, HIGH);
  digitalWrite(rclk, LOW);
  char text[] = "Bisimillah and I hope this workssss.";
  int len = sizeof(text)/sizeof(char) - 1;
  write_text(text, len);

  // write_char(0x86, 's');
  // write_char(0x87, 'x');
  // write_char(0x88, 'e');
  // write_char(0x89, 'l');
  // write_char(0x8A, ' ');
  // write_char(0x8B, ';');
  // write_char(0x8C, '_');
  // write_char(0x8D, ';'); 
  
  // delay(1000);
  // write_instruction(0b00010000);
  // delay(800);
  // write_instruction(0b00010000);
  // delay(800);
  // write_instruction(0b00010000);
  
  // delay(1000);

  // write_char(0x8B, ':');
  // delay(100);
  // write_char(0x8C, 'D');
  // delay(100);
  // write_char(0x8D, '^');

  // write_data(0b10100000);
  // write_data(0b10101010);
}

void write_text(char* str, int strlen) {
  if ((cursor + strlen) > 0x4f) {
    cursor = 0x00;
    clear_display();
  }
  for (int i = 0; i < strlen; i ++) {
    write_char(cursor + i, str[i]);
    if ((cursor + i) > 0x0F && (cursor + i) < 0x40) {
      write_instruction(0x80 | 0x40);
      cursor = 0x40;
    }
  }
}

void write_char(int pos, unsigned char c) {
  // write_instruction(pos | 0x80);
  delay(100);
  write_data(c);
}

void set_display() {
  unsigned char data = 0b00001111;
  write_instruction(data);
}


void clear_display() {
  unsigned char data = 0b00000001;
  write_instruction(data);
  delay(2);
}

void init_mode() {
  unsigned char data = 0b00111000;
  write_instruction(data);
}

void write_instruction(unsigned char data) {
  digitalWrite(rs, LOW);
  shiftOut(out, srclk, MSBFIRST, data);
  digitalWrite(rclk, LOW);
  digitalWrite(rclk, HIGH);
  digitalWrite(rclk, LOW);
  digitalWrite(e, LOW);
  digitalWrite(e, HIGH);
  digitalWrite(e, LOW);
  delayMicroseconds(40);
}

void write_data(unsigned char data) {
  digitalWrite(rs, HIGH);
  shiftOut(out, srclk, MSBFIRST, data);
  digitalWrite(rclk, LOW);
  digitalWrite(rclk, HIGH);
  digitalWrite(rclk, LOW);
  digitalWrite(e, LOW);
  digitalWrite(e, HIGH);
  digitalWrite(e, LOW);
  delayMicroseconds(37);
}



void loop() {
  // put your main code here, to run repeatedly:
}