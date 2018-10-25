import argparse
import scapy.all as scapy

parser = argparse.ArgumentParser(description='Monitor telnet connection between two hosts and display the content.')
parser.add_argument('host1', help='First host IP address')
parser.add_argument('host2', help='Second host IP address')
args = parser.parse_args()

scapy.sniff(filter="tcp and port 23 and host {0} and host {1}".format(args.host1, args.host2), prn=lambda x: x.sprintf("{IP:%IP.src% -> %IP.dst%\n}{%TCP.payload%\n}"))