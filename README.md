# Python ARP Spoofer

## Spoof ARP requests between clients

Port forwarding must be enabled
```
sudo echo 1 > /proc/sys/net/ipv4/ip_forward
```

Required module:
```  
pip install scapy
```

Download the script
```
wget https://github.com/DGclasher/py-arp-spoofer/raw/main/py-spoofer.py
```

Use --help to get info about the arguments
```
sudo python3 py-spoofer.py --help
```
```
sudo python py-spoofer.py -i [Interface] -t [Target IP] -s [Spoof IP/ Gateway IP]
```
