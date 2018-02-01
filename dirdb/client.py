from dirdb.constants import MSGLEN
from threading import Thread
import socket
import json


class Client(Thread):

    def __init__(self, host='localhost', port=7768):
        Thread.__init__(self)

        self.socket = None
        self.killed = False
        self.host = host
        self.port = port

    def run(self):
        self.socket = socket.socket()
        self.socket.connect((self.host, self.port))
        print('Connected to', self.host)

        while not self.killed:
            cli_input = raw_input("message: ")
            self.socket.send(cli_input)

            incoming = self.socket.recv(MSGLEN)

            print(json.loads(incoming))
