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


# connect
ss = serial.Serial('COM3', 9600)
time.sleep(1) # wait 1 second to ensure connection
ss.read(1)


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


with uinput.UInput() as ui:
    while True:
        try:
            # load button states
            btns = bytearray([0,0,0,0])
            for b in range(0,PAYLOAD_SIZE):
                btns[b] = ord(ss.read(1))
                print('{0:08b}'.format(btns[b]), end=' ') # debugging: print binary representation of bytes
                print()

            #byte0
            ui.write(e.EV_KEY, e.KEY_UP,         (btns[0] & 0b10000000) >> 7)
            ui.write(e.EV_KEY, e.KEY_DOWN,       (btns[0] & 0b01000000) >> 6)
            ui.write(e.EV_KEY, e.KEY_LEFT,       (btns[0] & 0b00100000) >> 5)
            ui.write(e.EV_KEY, e.KEY_RIGHT,      (btns[0] & 0b00010000) >> 4)
            ui.write(e.EV_KEY, e.KEY_W,          (btns[0] & 0b00001000) >> 3)
            ui.write(e.EV_KEY, e.KEY_A,          (btns[0] & 0b00000100) >> 2)
            ui.write(e.EV_KEY, e.KEY_S,          (btns[0] & 0b00000010) >> 1)
            ui.write(e.EV_KEY, e.KEY_D,          (btns[0] & 0b00000001))
            #byte1
            ui.write(e.EV_KEY, e.KEY_5,          (btns[1] & 0b10000000) >> 7)
            ui.write(e.EV_KEY, e.KEY_1,          (btns[1] & 0b01000000) >> 6)
            ui.write(e.EV_KEY, e.KEY_L,          (btns[1] & 0b00100000) >> 5)
            ui.write(e.EV_KEY, e.KEY_SEMICOLON,  (btns[1] & 0b00010000) >> 4)
            ui.write(e.EV_KEY, e.KEY_APOSTROPHE, (btns[1] & 0b00001000) >> 3)
            ui.write(e.EV_KEY, e.KEY_COMMA,      (btns[1] & 0b00000100) >> 2)
            ui.write(e.EV_KEY, e.KEY_SLASH,      (btns[1] & 0b00000010) >> 1)
            ui.write(e.EV_KEY, e.KEY_DOT,        (btns[1] & 0b00000001))
            #byte2
            ui.write(e.EV_KEY, e.KEY_M,          (btns[2] & 0b10000000) >> 7)
            ui.write(e.EV_KEY, e.KEY_6,          (btns[2] & 0b01000000) >> 6)
            ui.write(e.EV_KEY, e.KEY_2,          (btns[2] & 0b00100000) >> 5)
            ui.write(e.EV_KEY, e.KEY_T,          (btns[2] & 0b00010000) >> 4)
            ui.write(e.EV_KEY, e.KEY_Y,          (btns[2] & 0b00001000) >> 3)
            ui.write(e.EV_KEY, e.KEY_U,          (btns[2] & 0b00000100) >> 2)
            ui.write(e.EV_KEY, e.KEY_G,          (btns[2] & 0b00000010) >> 1)
            ui.write(e.EV_KEY, e.KEY_H,          (btns[2] & 0b00000001))
            #byte3
            ui.write(e.EV_KEY, e.KEY_J,          (btns[3] & 0b10000000) >> 7)
            ui.write(e.EV_KEY, e.KEY_F,          (btns[3] & 0b01000000) >> 6)
            ui.write(e.EV_KEY, e.KEY_P,          (btns[3] & 0b00100000) >> 5)

            #TODO system macros

            ui.syn()
        except serial.serialutil.SerialException:
            release_keys(ui)
            ss.close()
