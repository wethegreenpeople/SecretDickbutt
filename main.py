from PIL import Image
import random
import shutil
import getpass
import schedule
import time
import os
import ctypes
from ctypes import wintypes
import logging

username = getpass.getuser()
dest="C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\info.log"
logging.basicConfig(filename=dest,level=logging.INFO)
logger = logging.getLogger(__name__)
dickButtsAdded = 0

def SetWallpaper(i=[0]):
	username = getpass.getuser()
	drive = "c:\\"
	folder = "Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes"
	image = "dickbuttified.png"
	image_path = os.path.join(drive, folder, image)
	try:
		logging.info("Setting new wallpaper")
		SPI_SETDESKWALLPAPER  = 0x0014
		SPIF_UPDATEINIFILE    = 0x0001
		SPIF_SENDWININICHANGE = 0x0002

		user32 = ctypes.WinDLL('user32')
		SystemParametersInfo = user32.SystemParametersInfoW
		SystemParametersInfo.argtypes = ctypes.c_uint,ctypes.c_uint,ctypes.c_void_p,ctypes.c_uint
		SystemParametersInfo.restype = wintypes.BOOL
		SystemParametersInfo(SPI_SETDESKWALLPAPER, 0, image_path, SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
		# Keeping track of how many dickbutts should be in the wallpaper
		i[0] += 1
		logging.info(str([i[0]]) + " dickbutts added")
	except Exception as e:
		logging.info("Could not set wallpaper")
		logging.debug(e)


def DickButtify():
	username = getpass.getuser()

	try:
		# Copying the current wallpaper to our working folder to be edited
		logging.info("Grabbing current wallpaper")
		source="C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
		dest="C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\wallpaper.jpg"
		shutil.copy(source,dest)
		
		wallpaper = Image.open("C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\wallpaper.jpg").convert("RGBA")
		dickbutt = Image.open(str(resource_path("mask.png"))).convert("RGBA")
		size = random.randint(100,300)
		dickbutt = dickbutt.resize((size,size))

		# Location of dickbutt on wallpaper. Subtracting 200 to make sure you always see full dickbutt
		locA = random.randint(0,wallpaper.width - 50)
		locB = random.randint(0,wallpaper.height - 50)

		logging.info("Adding dickbutt at: " + str(locA) + ", " + str(locB))
		wallpaper.paste(dickbutt, (locA,locB), dickbutt)
		#wallpaper.show()
		logging.info("Saving dickbuttified wallaper")
		wallpaper.save("C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\" + "dickbuttified.png", format="png")
	except Exception as e:
		logging.info("Could not dickbuttify")
		logging.debug(e)

def CopyRename():
	username = getpass.getuser()
	source="C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\TranscodedWallpaper"
	dest="C:\\Users\\" + str(username) + "\\AppData\\Roaming\\Microsoft\\Windows\\Themes\\tmp.jpg"
	try:
		# if tmp.jpg already exists we don't want to write over it with our dirty dickbutt wallpaper
		if os.path.isfile(dest) == False:
			logging.info("Saving copy of original wallpaper")
			shutil.copy(source,dest)
		elif os.path.isfile(dest) == True:
			logging.info("Original wallpaper already saved")
	except Exception as e:
		logging.info("Could not backup original wallpaper")
		logging.debug(e)

def resource_path(relative_path):
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

CopyRename()
DickButtify()
SetWallpaper()
schedule.every().hour.do(DickButtify)
schedule.every().hour.do(SetWallpaper)
while True:
	schedule.run_pending()
	time.sleep(60)
