# Python ARP Spoofer
------------------------------
# Spoof ARP requests between clients using this script

------------------------------
This python script just works like any other arp spoofer but in a more convenient way.

Before running this, you must enable port forwarding in your machine
To do that
For Linux:

    sudo echo 1 > /proc/sys/net/ipv4/ip_forward

   * If it says permission denied then upgrade yourself to root user

After performing that, you must install the scapy module

For Python 2:
    
    pip install scapy

For Python 3:
    
    pip3 install scapy

After that, download the script:

    wget https://github.com/DGclasher/py-arp-spoofer/raw/main/py-spoofer.py

You can run this script either with python2 or python3
If you need help with arguements to provide, use --help 

    sudo python py-spoofer.py --help

Operation:

    sudo python py-spoofer.py -i [Interface] -t [Target IP] -s [Spoof IP/ Gateway IP]

You can use CTRL C/ CTRL Z to stop this script

*Note: This script is not meant for any unethical practices, I would not be held responsible for any misuse of this script*
----------------------------------------------------------------------------------------------------------------------
