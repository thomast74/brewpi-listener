import ConfigParser
import ipaddr
import select
import socket
import sys


config = ConfigParser.RawConfigParser()
config.read("BrewPiListener.cfg")

PORT = config.getint('server', 'port')
data = "{" \
       "  \"version\": \"0.1\", " \
       "  \"revision\": \"C\", " \
       "  \"device-id\": \"xx-xx-xx-xx-xx\", " \
       "  \"ip-address\": \"0.1\", " \
       "  \"status\": \"ACTIVE\" " \
       "}"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

print "\nSending data to 192.168.2.255"
sock.sendto(data + "\n", ("192.168.2.255", PORT))

print "Sent:     {}".format(data)
ready = select.select([sock], [], [], 1)
if ready[0]:
    data = sock.recv(512)
    print "Received: {}".format(data)
