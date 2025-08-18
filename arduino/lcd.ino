int rs = 4;   // H: data, L: instruction code
int e = 5;    // H,H -> L chip enable signal
int out = 12;  // data pin to 8 bit shift reg
int rclk = 3;
int srclk = 2;

void setup() {
  pinMode(rs, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(out, OUTPUT);
  pinMode(rclk, OUTPUT);
  pinMode(srclk, OUTPUT);

  shiftOut(out, srclk, MSBFIRST, 0);
  digitalWrite(rclk, LOW);
  digitalWrite(rclk, HIGH);
  digitalWrite(rclk, LOW);

  init_mode();
  clear_display();
  set_display();
  delay(1000);
  write_char(0x80, 's');
  write_char(0x81, 't');
  write_char(0x82, 'r');
  write_char(0x83, 'e');
  write_char(0x84, 'a');
  write_char(0x85, 'k');
  write_char(0x86, 's');
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
  
  delay(1000);

  write_char(0x8B, ':');
  delay(100);
  write_char(0x8C, 'D');
  delay(100);
  // write_char(0x8D, '^');
}

void write_char(int pos, unsigned char c) {
  write_instruction(pos);
  delay(200);
  write_data(c);
}

void set_display() {
  unsigned char data = B00001111;
  write_instruction(data);
}


void clear_display() {
  unsigned char data = 0x1;
  write_instruction(data);
}

void init_mode() {
  unsigned char data = 0b00111100;
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
  delay(0.037);
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
}



void loop() {
  // put your main code here, to run repeatedly:
}
