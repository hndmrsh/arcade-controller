/*
 * Payload description:
 *   4 bytes per packet; described from MSB to LSB
 * 
 * Byte0:
 *   P1_UP
 *   P1_DOWN
 *   P1_LEFT
 *   P1_RIGHT
 *   P2_UP
 *   P2_DOWN
 *   P2_LEFT
 *   P2_RIGHT
 *
 * Byte1:
 *   P1_COIN
 *   P1_START
 *   P1_B1
 *   P1_B2
 *   P1_B3
 *   P1_B4
 *   P1_B5
 *   P1_B6
 *
 * Byte2:
 *   P1_B7
 *   P2_COIN
 *   P2_START
 *   P2_B1
 *   P2_B2
 *   P2_B3
 *   P2_B4
 *   P2_B5
 *
 * Byte3:
 *   P2_B6
 *   P2_B7
 *   NONE
 *   NONE
 *   NONE
 *   NONE
 *   NONE
 *   NONE
 */

const int PAYLOAD_SIZE = 4;

const int PIN_P1_UP = 22;
const int PIN_P1_DOWN = 24;
const int PIN_P1_LEFT = 26;
const int PIN_P1_RIGHT = 28;
const int PIN_P2_UP = 23;
const int PIN_P2_DOWN = 25;
const int PIN_P2_LEFT = 27;
const int PIN_P2_RIGHT = 29;

const int PIN_P1_COIN = 30;
const int PIN_P1_START = 32;
const int PIN_P1_B1 = 34;
const int PIN_P1_B2 = 36;
const int PIN_P1_B3 = 38;
const int PIN_P1_B4 = 40;
const int PIN_P1_B5 = 42;
const int PIN_P1_B6 = 44;

const int PIN_P1_B7 = 46;
const int PIN_P2_COIN = 31;
const int PIN_P2_START = 33;
const int PIN_P2_B1 = 35;
const int PIN_P2_B2 = 37;
const int PIN_P2_B3 = 39;
const int PIN_P2_B4 = 41;
const int PIN_P2_B5 = 43;

const int PIN_P2_B6 = 45;
const int PIN_P2_B7 = 47;

byte btns[PAYLOAD_SIZE];

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  pinMode(PIN_P1_UP, INPUT);
  pinMode(PIN_P1_DOWN, INPUT);
  pinMode(PIN_P1_LEFT, INPUT);
  pinMode(PIN_P1_RIGHT, INPUT);
  pinMode(PIN_P2_UP, INPUT);
  pinMode(PIN_P2_DOWN, INPUT);
  pinMode(PIN_P2_LEFT, INPUT);
  pinMode(PIN_P2_RIGHT, INPUT);
  pinMode(PIN_P1_COIN, INPUT);
  pinMode(PIN_P1_START, INPUT);
  pinMode(PIN_P1_B1, INPUT);
  pinMode(PIN_P1_B2, INPUT);
  pinMode(PIN_P1_B3, INPUT);
  pinMode(PIN_P1_B4, INPUT);
  pinMode(PIN_P1_B5, INPUT);
  pinMode(PIN_P1_B6, INPUT);
  pinMode(PIN_P1_B7, INPUT);
  pinMode(PIN_P2_COIN, INPUT);
  pinMode(PIN_P2_START, INPUT);
  pinMode(PIN_P2_B1, INPUT);
  pinMode(PIN_P2_B2, INPUT);
  pinMode(PIN_P2_B3, INPUT);
  pinMode(PIN_P2_B4, INPUT);
  pinMode(PIN_P2_B5, INPUT);
  pinMode(PIN_P2_B6, INPUT);
  pinMode(PIN_P2_B7, INPUT);
}


void loop() {
  if(Serial) {    
    for(int b = 0; b < PAYLOAD_SIZE; b++) {
  	  btns[b] = 0;
  	}
      
    btns[0] |= (buttonState(PIN_P1_UP) << 7);
    btns[0] |= (buttonState(PIN_P1_DOWN) << 6);
    btns[0] |= (buttonState(PIN_P1_LEFT) << 5);
    btns[0] |= (buttonState(PIN_P1_RIGHT) << 4);
    btns[0] |= (buttonState(PIN_P2_UP) << 3);
    btns[0] |= (buttonState(PIN_P2_DOWN) << 2);
    btns[0] |= (buttonState(PIN_P2_LEFT) << 1);
    btns[0] |= (buttonState(PIN_P2_RIGHT));
    btns[1] |= (buttonState(PIN_P1_COIN) << 7);
    btns[1] |= (buttonState(PIN_P1_START) << 6);
    btns[1] |= (buttonState(PIN_P1_B1) << 5);
    btns[1] |= (buttonState(PIN_P1_B2) << 4);
    btns[1] |= (buttonState(PIN_P1_B3) << 3);
    btns[1] |= (buttonState(PIN_P1_B4) << 2);
    btns[1] |= (buttonState(PIN_P1_B5) << 1);
    btns[1] |= (buttonState(PIN_P1_B6));
    btns[2] |= (buttonState(PIN_P1_B7) << 7);
    btns[2] |= (buttonState(PIN_P2_COIN) << 6);
    btns[2] |= (buttonState(PIN_P2_START) << 5);
    btns[2] |= (buttonState(PIN_P2_B1) << 4);
    btns[2] |= (buttonState(PIN_P2_B2) << 3);
    btns[2] |= (buttonState(PIN_P2_B3) << 2);
    btns[2] |= (buttonState(PIN_P2_B4) << 1);
    btns[2] |= (buttonState(PIN_P2_B5));
    btns[3] |= (buttonState(PIN_P2_B6) << 7);
    btns[3] |= (buttonState(PIN_P2_B7) << 6);

    Serial.write(btns, PAYLOAD_SIZE);
  }
}

int buttonState(int pin) {
  if(digitalRead(pin) == HIGH) {
    return 1;
  }

  return 0;
}
