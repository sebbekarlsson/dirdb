from threading import Thread
import json


MSGLEN = 2048 * 7


class Connection(Thread):

    def __init__(self, socket, server):
        Thread.__init__(self)

        self.socket = socket
        self.server = server

    def run(self):
        while True:
            incoming = self.socket.recv(MSGLEN)

            try:
                data = json.loads(incoming)
            except ValueError:
                self.socket.close()
                self.socket = None

                continue

            print(data)
