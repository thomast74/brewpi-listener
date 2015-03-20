# Copyright 2015 Oink Brew
# This file is part of Oink Brew.

# Oink Brew is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Oink Brew is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Oink Brew Listener.
# If not, see <http://www.gnu.org/licenses/gpl.html>.
#
# @author Thomas Trageser


import ConfigParser
import ipaddr
import select
import socket
import sys


def main():
    config = ConfigParser.RawConfigParser()
    config.read("oinkbrew_listener.cfg")

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

    print "\nSending data to 0.0.0.0.255"
    sock.sendto(data + "\n", ("0.0.0.0", PORT))

    print "Sent:     {}".format(data)
    ready = select.select([sock], [], [], 1)
    if ready[0]:
        data = sock.recv(512)
        print "Received: {}".format(data)


if __name__ == "__main__":
    main()
