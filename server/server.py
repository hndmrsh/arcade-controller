import serial
import time
import win32api
import win32con

f = 0x46 # VirtualKey Code of the letter "F", see http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx 
g = 0x47 # VirtualKey Code of the letter "F", see http://msdn.microsoft.com/en-us/library/windows/desktop/dd375731%28v=vs.85%29.aspx 

ss = serial.Serial('COM3', 9600)
time.sleep(1)

while 1:
	try:
		val = ss.read()
		print('{0:08b}'.format(ord(val)))

		if ord(val) & 0b10000000 > 0:
			win32api.keybd_event(f,0,0,0)
			win32api.keybd_event(f,0,win32con.KEYEVENTF_KEYUP,0)
		if ord(val) & 0b01000000 > 0:
			win32api.keybd_event(g,0,0,0)
			win32api.keybd_event(g,0,win32con.KEYEVENTF_KEYUP,0)

	except ss.SerialTimeoutException:
		print('Data could not be read')