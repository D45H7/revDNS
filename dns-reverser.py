#!/usr/bin/python3

import requests as req, os

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

