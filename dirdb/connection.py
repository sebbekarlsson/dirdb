from dirdb.constants import MSGLEN
from threading import Thread


class Connection(Thread):

    def __init__(self, socket, server):
        Thread.__init__(self)

        self.socket = socket
        self.server = server

    def run(self):
        while True:
            incoming = self.socket.recv(MSGLEN)

            response = self.server.query_handler.execute(incoming)
            self.socket.send(response)
