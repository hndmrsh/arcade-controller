# See controller-client.ino for a description of the serial payload.
#
# Button mapping:
#
# P1_UP = up
# P1_DOWN = down
# P1_LEFT = left
# P1_RIGHT = right
# P1_COIN = 5
# P1_START = 1
# P1_B1 = L
# P1_B2 = ;
# P1_B3 = '
# P1_B4 = ,
# P1_B5 = .
# P1_B6 = /
# P1_B7 = M
#
# P2_UP = W
# P2_DOWN = S
# P2_LEFT = A
# P2_RIGHT = D
# P2_COIN = 6
# P2_START = 2
# P2_B1 = T
# P2_B2 = Y
# P2_B3 = U
# P2_B4 = G
# P2_B5 = H
# P2_B6 = J
# P2_B7 = F
#
# System buttons will be used for macros, and have no simple mapping

import serial
import time
from evdev import uinput, ecodes as e


PAYLOAD_SIZE = 4


def release_keys(ui):
    ui.write(e.EV_KEY, e.KEY_UP,         0)
    ui.write(e.EV_KEY, e.KEY_DOWN,       0)
    ui.write(e.EV_KEY, e.KEY_LEFT,       0)
    ui.write(e.EV_KEY, e.KEY_RIGHT,      0)
    ui.write(e.EV_KEY, e.KEY_W,          0)
    ui.write(e.EV_KEY, e.KEY_A,          0)
    ui.write(e.EV_KEY, e.KEY_S,          0)
    ui.write(e.EV_KEY, e.KEY_D,          0)
    ui.write(e.EV_KEY, e.KEY_5,          0)
    ui.write(e.EV_KEY, e.KEY_1,          0)
    ui.write(e.EV_KEY, e.KEY_L,          0)
    ui.write(e.EV_KEY, e.KEY_SEMICOLON,  0)
    ui.write(e.EV_KEY, e.KEY_APOSTROPHE, 0)
    ui.write(e.EV_KEY, e.KEY_COMMA,      0)
    ui.write(e.EV_KEY, e.KEY_SLASH,      0)
    ui.write(e.EV_KEY, e.KEY_DOT,        0)
    ui.write(e.EV_KEY, e.KEY_M,          0)
    ui.write(e.EV_KEY, e.KEY_6,          0)
    ui.write(e.EV_KEY, e.KEY_2,          0)
    ui.write(e.EV_KEY, e.KEY_T,          0)
    ui.write(e.EV_KEY, e.KEY_Y,          0)
    ui.write(e.EV_KEY, e.KEY_U,          0)
    ui.write(e.EV_KEY, e.KEY_G,          0)
    ui.write(e.EV_KEY, e.KEY_H,          0)
    ui.write(e.EV_KEY, e.KEY_J,          0)
    ui.write(e.EV_KEY, e.KEY_F,          0)
    ui.write(e.EV_KEY, e.KEY_P,          0)
    ui.syn()

# connect
ss = serial.Serial('/dev/ttyUSB0', 9600)
time.sleep(2) # wait 2 second to ensure connection



with uinput.UInput() as ui:

    # we know the payload when all buttons are off is 
    # 11111111 11111111 11111111 11111100
    # so flush all bytes until we see the last byte of a payload
    while True:
        flush = ord(ss.read(1))
        print flush
        if flush == 0b11111100:
            break

    while True:
        try:
            # load button states
            btns = bytearray([0,0,0,0])
            btn_str = ""
            for b in range(0,PAYLOAD_SIZE):
                btns[b] = ord(ss.read(1))
                btn_str += '{0:08b} '.format(btns[b]) # debugging: print binary representation of bytes
            print btn_str

            #byte0
            ui.write(e.EV_KEY, e.KEY_UP,         1-((btns[0] & 0b10000000) >> 7))
            ui.write(e.EV_KEY, e.KEY_DOWN,       1-((btns[0] & 0b01000000) >> 6))
            ui.write(e.EV_KEY, e.KEY_LEFT,       1-((btns[0] & 0b00100000) >> 5))
            ui.write(e.EV_KEY, e.KEY_RIGHT,      1-((btns[0] & 0b00010000) >> 4))
            ui.write(e.EV_KEY, e.KEY_W,          1-((btns[0] & 0b00001000) >> 3))
            ui.write(e.EV_KEY, e.KEY_A,          1-((btns[0] & 0b00000100) >> 2))
            ui.write(e.EV_KEY, e.KEY_S,          1-((btns[0] & 0b00000010) >> 1))
            ui.write(e.EV_KEY, e.KEY_D,          1-((btns[0] & 0b00000001)))
            #byte1
            ui.write(e.EV_KEY, e.KEY_5,          1-((btns[1] & 0b10000000) >> 7))
            ui.write(e.EV_KEY, e.KEY_1,          1-((btns[1] & 0b01000000) >> 6))
            ui.write(e.EV_KEY, e.KEY_L,          1-((btns[1] & 0b00100000) >> 5))
            ui.write(e.EV_KEY, e.KEY_SEMICOLON,  1-((btns[1] & 0b00010000) >> 4))
            ui.write(e.EV_KEY, e.KEY_APOSTROPHE, 1-((btns[1] & 0b00001000) >> 3))
            ui.write(e.EV_KEY, e.KEY_COMMA,      1-((btns[1] & 0b00000100) >> 2))
            ui.write(e.EV_KEY, e.KEY_SLASH,      1-((btns[1] & 0b00000010) >> 1))
            ui.write(e.EV_KEY, e.KEY_DOT,        1-((btns[1] & 0b00000001)))
            #byte2
            ui.write(e.EV_KEY, e.KEY_M,          1-((btns[2] & 0b10000000) >> 7))
            ui.write(e.EV_KEY, e.KEY_6,          1-((btns[2] & 0b01000000) >> 6))
            ui.write(e.EV_KEY, e.KEY_2,          1-((btns[2] & 0b00100000) >> 5))
            ui.write(e.EV_KEY, e.KEY_T,          1-((btns[2] & 0b00010000) >> 4))
            ui.write(e.EV_KEY, e.KEY_Y,          1-((btns[2] & 0b00001000) >> 3))
            ui.write(e.EV_KEY, e.KEY_U,          1-((btns[2] & 0b00000100) >> 2))
            ui.write(e.EV_KEY, e.KEY_G,          1-((btns[2] & 0b00000010) >> 1))
            ui.write(e.EV_KEY, e.KEY_H,          1-((btns[2] & 0b00000001)))
            #byte3
            ui.write(e.EV_KEY, e.KEY_J,          1-((btns[3] & 0b10000000) >> 7))
            ui.write(e.EV_KEY, e.KEY_F,          1-((btns[3] & 0b01000000) >> 6))
            ui.write(e.EV_KEY, e.KEY_P,          1-((btns[3] & 0b00100000) >> 5))

            #TODO system macros

            ui.syn()
        except serial.serialutil.SerialException:
            release_keys(ui)
            ss.close()
