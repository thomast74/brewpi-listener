import json
import logging
import requests
import SocketServer
import sys


# global variables
POST_URL = ""


class BrewPiListenerRequestHandler(SocketServer.BaseRequestHandler):

    logger = logging.getLogger("BrewPiListenerRequestHandler")

    # UDP request coming in
    def handle(self):
        try:
            json_string = self.request[0].strip()
            socket = self.request[1]

            self.logger.info("Handle message from {}".format(self.client_address[0]))

            if self.validate_json(json_string):
                self.logger.debug("Received Status from {}".format(self.client_address[0]))
                socket.sendto("OK", self.client_address)
                self.send_status_to_api_server(json_string)
            else:
                self.logger.error("Received Invalid Json Status")
                socket.sendto("ERROR", self.client_address)
        except:
            e = sys.exc_info()[0]
            self.logger.error(e)

    def validate_json(self, json_string):
        try:
            jsonData = json.loads(json_string)
            return True
        except ValueError:
            return False

    def send_status_to_api_server(self, status):
        try:
            # open connection and post json to http://localhost/breqpi/api/status
            self.logger.debug("POST to Url {}".format(POST_URL))

            response = requests.post(POST_URL, data=json.dumps(status))
            self.logger.debug("RESPONSE: {} {}".format(response.status_code, response.text))
        except:
            e = sys.exc_info()[0]
            self.logger.error(e)
