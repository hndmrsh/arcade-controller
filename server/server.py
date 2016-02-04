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

import serial
import time
import win32api
import win32con
import ctypes

# BLOCK: this block from http://stackoverflow.com/questions/14489013/simulate-python-keypresses-for-controlling-a-game

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

# END BLOCK

PAYLOAD_SIZE = 4

# DirectInput ScanCodes from http://www.gamespp.com/directx/directInputKeyboardScanCodes.html

VK_LEFT = 0xCB
VK_UP = 0xC8
VK_RIGHT = 0xCD
VK_DOWN = 0xD0
VK_1 = 0x31
VK_2 = 0x32
VK_5 = 0x35
VK_6 = 0x36
VK_A = 0x41
VK_D = 0x44
VK_F = 0x46
VK_G = 0x47
VK_H = 0x48
VK_J = 0x4A
VK_L = 0x4C
VK_M = 0x4D
VK_S = 0x53
VK_T = 0x54
VK_U = 0x55
VK_W = 0x57
VK_Y = 0x59
VK_SEMICOLON = 0xBA
VK_COMMA = 0XBC
VK_FULLSTOP = 0XBE
VK_SLASH = 0xBF
VK_QUOTE = 0xDE

ss = serial.Serial('COM3', 9600)
time.sleep(1) # wait 1 second to ensure connection

cached_btns = bytearray([0,0,0,0])
btns = bytearray([0,0,0,0])

def update_button_state( byte_num, mask, vkey ):
	if cached_btns[byte_num] & mask > btns[byte_num] & mask:
		# button released, send KEYUP event
		#win32api.keybd_event(vkey, 0, win32con.KEYEVENTF_KEYUP, 0)
		PressKey(vkey)
	elif btns[byte_num] & mask > cached_btns[byte_num] & mask:
		# button pressed, send KEYDOWN event
		#win32api.keybd_event(vkey, 0, 0, 0)
		ReleaseKey(vkey)

while True:
	try:
		cached_btns[:] = btns[:]; # cache buttons state

		# load button states
		btns = bytearray([0,0,0,0])
		for b in range(0,PAYLOAD_SIZE):
			btns[b] = ord(ss.read(1))
			print('{0:08b}'.format(btns[b]), end=' ') # debugging: print binary representation of bytes
		print()

		# byte0
		update_button_state(1, 0b10000000, VK_UP)
		update_button_state(1, 0b01000000, VK_DOWN)
		update_button_state(1, 0b00100000, VK_LEFT)
		update_button_state(1, 0b00010000, VK_RIGHT)
		update_button_state(1, 0b00001000, VK_W)
		update_button_state(1, 0b00000100, VK_S)
		update_button_state(1, 0b00000010, VK_A)
		update_button_state(1, 0b00000001, VK_D)
		# byte1
		update_button_state(2, 0b10000000, VK_5)
		update_button_state(2, 0b01000000, VK_1)
		update_button_state(2, 0b00100000, VK_L)
		update_button_state(2, 0b00010000, VK_SEMICOLON)
		update_button_state(2, 0b00001000, VK_QUOTE)
		update_button_state(2, 0b00000100, VK_COMMA)
		update_button_state(2, 0b00000010, VK_SLASH)
		update_button_state(2, 0b00000001, VK_FULLSTOP)
		# byte2mm62tttt
		update_button_state(3, 0b10000000, VK_M)
		update_button_state(3, 0b01000000, VK_6)
		update_button_state(3, 0b00100000, VK_2)
		update_button_state(3, 0b00010000, VK_T)
		update_button_state(3, 0b00001000, VK_Y)
		update_button_state(3, 0b00000100, VK_U)
		update_button_state(3, 0b00000010, VK_G)
		update_button_state(3, 0b00000001, VK_H)
		# byte3
		update_button_state(0, 0b10000000, VK_J)
		update_button_state(0, 0b01000000, VK_F)

	except serial.serialutil.SerialException:
		release_keys()
		ss.close()




