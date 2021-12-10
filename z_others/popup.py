import os
import ctypes  # An included library with Python install.
if os.path.isfile (r"E:\sem_1"):
    pass
else:
    ctypes.windll.user32.MessageBoxW(0, "SD card was removed", "Your title", 1)