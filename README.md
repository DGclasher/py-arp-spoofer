# Python ARP Spoofer
------------------------------
# Spoof ARP requests between clients using this script
------------------------------
This python script just works like any other arp spoofer but in a more convenient way.

Port forwarding must be enabled

To do that:

    sudo echo 1 > /proc/sys/net/ipv4/ip_forward

   * If it says permission denied then upgrade yourself to root user

Required module:
  
    pip install scapy

After that, download the script:

    wget https://github.com/DGclasher/py-arp-spoofer/raw/main/py-spoofer.py

Use --help to see the required arguements: 

    sudo python3 py-spoofer.py --help

Operation:

    sudo python py-spoofer.py -i [Interface] -t [Target IP] -s [Spoof IP/ Gateway IP]

Use CTRL C/ CTRL Z to stop this script

----------------------------------------------------------------------------------------------------------------------
