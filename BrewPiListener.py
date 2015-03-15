import ConfigParser
import logging
import RequestHandler
import SocketServer
import sys
import threading


from daemon import runner


class ThreadedUDPServer(SocketServer.ThreadingMixIn, SocketServer.UDPServer):
    pass


class BrewPiListenerApp():

    logger = logging.getLogger("BrewListenerApp")
    ip_address = "192.168.2.255"
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
        server = ThreadedUDPServer((self.ip_address, self.port), RequestHandler.BrewPiListenerRequestHandler)

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
    RequestHandler.POST_URL = config.get('server', 'post-url')

    # setup logging
    log_level = config.get('server', 'log-level')
    numeric_level = getattr(logging, log_level.upper(), None)

    if not isinstance(numeric_level, int):
        raise ValueError('Invalid log level: %s' % log_level)

    logging.basicConfig(filename=config.get("server", "log-file"), filemode="a+", level=numeric_level,
                        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    # start daemon
    logging.info("Starting up application")
    app = BrewPiListenerApp(config.get("server", "ip-address"), config.getint("server", "port"),
                          config.get("server", "pid-file"), config.get("server", "out-log-file"),
                          config.get("server", "err-log-file"))
    daemon_runner = runner.DaemonRunner(app)
    daemon_runner.daemon_context.files_preserve = [logging.root.handlers[0].stream]
    daemon_runner.do_action()

if __name__ == "__main__":
    main(sys.argv[2])
