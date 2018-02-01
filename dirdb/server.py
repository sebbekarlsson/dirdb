from dirdb.query_handler import QueryHandler
from dirdb.connection import Connection
from threading import Thread
import socket
import os


class Server(Thread):

    def __init__(self, base_dir, host='localhost', port=7768):
        Thread.__init__(self)

        self.killed = False
        self.socket = None
        self.query_handler = QueryHandler()
        self.connections = []
        self.base_dir = base_dir
        self.host = host
        self.port = port

        if not os.path.isdir(self.base_dir):
            os.mkdir(self.base_dir)

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        c = None

        while not self.killed:
            self.socket.listen(5)
            print('Waiting for connections...')

            c, addr = self.socket.accept()
            print('Got connection from', addr)

            connection = Connection(socket=c, server=self)
            connection.setDaemon(True)
            connection.start()
            self.connections.append(connection)
