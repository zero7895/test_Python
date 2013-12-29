import win32gui
x,y=win32gui.GetCursorPos()
print(x, y)


#set cursor
from ctypes import *

#click cursor
import win32api
import win32con
import time


win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y)

time.sleep(1)

windll.user32.SetCursorPos(x+100, y)


win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x+100, y)

