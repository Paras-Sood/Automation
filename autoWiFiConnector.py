import os
import sys
import time

saved_profiles=os.popen('netsh wlan show profiles').read() # Show all the saved networks
print(saved_profiles)

available_networks=os.popen('netsh wlan show networks').read() # Show all the available networks
print(available_networks)

preffered_ssid=input("Enter the preferred network : ")

if preffered_ssid not in saved_profiles:
    print(preffered_ssid+" not found. Couldn't connect!!")
    sys.exit()

ttime=0
print("Searching...")
# Will try for 1 min. If not connected, then exit.
while True:
    if ttime==60:
        print("\n"+preffered_ssid+" is not available right now!!")
        sys.exit()
    if preffered_ssid in available_networks:
        break
    time.sleep(2)
    ttime=ttime+2

disconnect=os.popen('netsh wlan disconnect').read() # Disconnect to the currently connected network
print(disconnect)

resp=os.popen('netsh wlan connect name='+'"'+preffered_ssid+'"').read()
print(resp)
