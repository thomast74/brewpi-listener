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
import logging
import request_handler
import SocketServer
import sys
import threading


from daemon import runner
from request_handler import OinkBrewListenerRequestHandler

class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass


class OinkBrewListenerApp():

    logger = logging.getLogger("OinkBrewListenerApp")
    ip_address = "0.0.0.0"
    port = 7872

    def __init__(self, ip_address, port, pid_file, stdout, stderr):
        self.ip_address = ip_address
        self.port = port
        self.stdin_path = '/dev/null'
        self.stdout_path = stdout
        self.stderr_path = stderr
        self.pidfile_path = pid_file
        self.pidfile_timeout = 5

    def run(self):
        # Get configuration from CFG file

        # prepare UDP server
        self.logger.info("Listen to {}:{}".format(self.ip_address, self.port))
        server = ThreadedUDPServer((self.ip_address, self.port), OinkBrewListenerRequestHandler)

        # start UDP server
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True

        while True:
            if not server_thread.is_alive():
                server_thread.start()


def main(config_file):
    config = ConfigParser.RawConfigParser()
    config.read(config_file)

    # ser variables
    request_handler.POST_URL = config.get('server', 'post-url')

    # setup logging
    log_level = config.get('server', 'log-level')
    numeric_level = getattr(logging, log_level.upper(), None)

    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % log_level)

    logging.basicConfig(filename=config.get("server", "log-file"), filemode="a+", level=numeric_level,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # start daemon
    logging.info("Starting up application")
    app = OinkBrewListenerApp(config.get("server", "ip-address"), config.getint("server", "port"),
                              config.get("server", "pid-file"), config.get("server", "out-log-file"),
                              config.get("server", "err-log-file"))
    daemon_runner = runner.DaemonRunner(app)
    daemon_runner.daemon_context.files_preserve = [logging.root.handlers[0].stream]
    daemon_runner.do_action()


if __name__ == "__main__":
    main(sys.argv[2])
