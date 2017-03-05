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
 *   SYS_1
 *   SYS_2
 *   SYS_3
 *   SYS_4
 *   NONE
 *   NONE
 */

const int PAYLOAD_SIZE = 4;

const int PIN_P1_UP = 22;
const int PIN_P1_DOWN = 24;
const int PIN_P1_LEFT = 26;
const int PIN_P1_RIGHT = 28;
const int PIN_P1_B1 = 30;
const int PIN_P1_B2 = 32;
const int PIN_P1_B3 = 34;
const int PIN_P1_B4 = 36;
const int PIN_P1_B5 = 38;
const int PIN_P1_B6 = 40;
const int PIN_P1_B7 = 42;

const int PIN_P2_UP = 23;
const int PIN_P2_DOWN = 25;
const int PIN_P2_LEFT = 27;
const int PIN_P2_RIGHT = 29;
const int PIN_P2_B1 = 31;
const int PIN_P2_B2 = 33;
const int PIN_P2_B3 = 35;
const int PIN_P2_B4 = 37;
const int PIN_P2_B5 = 39;
const int PIN_P2_B6 = 41;
const int PIN_P2_B7 = 43;


const int PIN_P1_COIN = 44;
const int PIN_P1_START = 46;

const int PIN_P2_COIN = 45;
const int PIN_P2_START = 47;

const int PIN_SYS_1 = 48;
const int PIN_SYS_2 = 50;
const int PIN_SYS_3 = 49;
const int PIN_SYS_4 = 51;


byte btns[PAYLOAD_SIZE];

void setup() {
  // start serial port at 9600 bps:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  pinMode(PIN_P1_UP, INPUT_PULLUP);
  pinMode(PIN_P1_DOWN, INPUT_PULLUP);
  pinMode(PIN_P1_LEFT, INPUT_PULLUP);
  pinMode(PIN_P1_RIGHT, INPUT_PULLUP);
  pinMode(PIN_P2_UP, INPUT_PULLUP);
  pinMode(PIN_P2_DOWN, INPUT_PULLUP);
  pinMode(PIN_P2_LEFT, INPUT_PULLUP);
  pinMode(PIN_P2_RIGHT, INPUT_PULLUP);
  pinMode(PIN_P1_COIN, INPUT_PULLUP);
  pinMode(PIN_P1_START, INPUT_PULLUP);
  pinMode(PIN_P1_B1, INPUT_PULLUP);
  pinMode(PIN_P1_B2, INPUT_PULLUP);
  pinMode(PIN_P1_B3, INPUT_PULLUP);
  pinMode(PIN_P1_B4, INPUT_PULLUP);
  pinMode(PIN_P1_B5, INPUT_PULLUP);
  pinMode(PIN_P1_B6, INPUT_PULLUP);
  pinMode(PIN_P1_B7, INPUT_PULLUP);
  pinMode(PIN_P2_COIN, INPUT_PULLUP);
  pinMode(PIN_P2_START, INPUT_PULLUP);
  pinMode(PIN_P2_B1, INPUT_PULLUP);
  pinMode(PIN_P2_B2, INPUT_PULLUP);
  pinMode(PIN_P2_B3, INPUT_PULLUP);
  pinMode(PIN_P2_B4, INPUT_PULLUP);
  pinMode(PIN_P2_B5, INPUT_PULLUP);
  pinMode(PIN_P2_B6, INPUT_PULLUP);
  pinMode(PIN_P2_B7, INPUT_PULLUP);
  pinMode(PIN_SYS_1, INPUT_PULLUP);
  pinMode(PIN_SYS_2, INPUT_PULLUP);
  pinMode(PIN_SYS_3, INPUT_PULLUP);
  pinMode(PIN_SYS_4, INPUT_PULLUP);
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
    btns[3] |= (buttonState(PIN_SYS_1) << 5);
    btns[3] |= (buttonState(PIN_SYS_2) << 4);
    btns[3] |= (buttonState(PIN_SYS_3) << 3);
    btns[3] |= (buttonState(PIN_SYS_4) << 2);

    Serial.write(btns, PAYLOAD_SIZE);
  }
}

int buttonState(int pin) {
  if(digitalRead(pin) == HIGH) {
    return 1;
  }

  return 0;
}
