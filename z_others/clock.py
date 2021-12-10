import time
import subprocess as sp
from colorama import init

init()
from colorama import Fore

while True:
    localtime = time.localtime()
    # print (Fore.RED +	"red text" + Fore.YELLOW + " other text" + Fore.RESET)
    result = time.strftime("%I:%M:%S %p", localtime)
    print(Fore.BLUE + result.split(":")[0] + ":" +
          Fore.YELLOW + result.split(":")[1] + ":" +
          Fore.RED + result.split(":")[2] + Fore.RESET
          )
    time.sleep(1)
    sp.call('cls', shell=True)
