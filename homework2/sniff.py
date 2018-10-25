import argparse
import scapy.all as scapy

parser = argparse.ArgumentParser(description='Launch SYN DOS attack.')
parser.add_argument('target', help='The IP address of the target')
args = parser.parse_args()

print(scapy.sniff(filter="(TCP or UDP) and host {0}".format(args.target), count=2))