const int PIN_1_START = 10;
const int PIN_1_COIN = 11;

byte btns;

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  pinMode(PIN_1_START, INPUT);
  pinMode(PIN_1_COIN, INPUT);

  pinMode(13, OUTPUT); // debugging
  
}


void loop() {
  if(Serial) {
    btns = 0;
    
    if(digitalRead(PIN_1_START) == HIGH) {
      btns |= (1 << 7);
    }

    if(digitalRead(PIN_1_COIN) == HIGH) {
      btns |= (1 << 6);
    }

    Serial.write(btns);
  }
}
