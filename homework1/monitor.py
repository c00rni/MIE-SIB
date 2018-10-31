import argparse
import scapy.all as scapy

parser = argparse.ArgumentParser(description='Monitor telnet message sent to a client to a server.')
parser.add_argument('client', help='telnet client IP address')
parser.add_argument('server', help='telnet server IP address')
args = parser.parse_args()

scapy.sniff(filter="tcp and port 23 and src {0} and dst {1}".format(args.client, args.server), prn=lambda x:x.sprintf("[{IP:%IP.src% -> %IP.dst%}]: {Raw:%Raw.load%}"))
