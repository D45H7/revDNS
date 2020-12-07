#!/usr/bin/python3
# dns reverser tool
# by EtcAug10 from hackertarget's api
#

import os

try:
	import requests as req
except:
	print("Lib requests tidak ada. Menginstall..")
	os.system("pip install requests")

def ekse(target):
    r = req.get(target)
    resp = r.text
    print("Hasil: \n"+resp)

banner = """
/(    --------   )\\
|  DNS Reverser   |
|    EtcAug10     |
\_________________/
"""

os.system('clear')
print(banner)
ip = input("\nMasukkan alamat IP: ")
target = "https://api.hackertarget.com/reversedns/?q=" + ip

ekse(target)
