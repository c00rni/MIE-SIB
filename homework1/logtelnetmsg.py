import argparse
import scapy.all as scapy

parser = argparse.ArgumentParser(description='Log the content of a telnet connection without any password')
parser.add_argument('host1', help='First host IP address')
parser.add_argument('host2', help='Second host IP address')
args = parser.parse_args()

packets = scapy.sniff(filter="tcp and port 23 and host {0} and host {1}".format(args.host1, args.host2), count=5)

with open('output.txt', mode='a') as log_file:
    for num_packet in range(len(packets)):
        try:
            log_file.write(packets[num_packet]['Raw'].load.decode())
        except IndexError:
            pass

