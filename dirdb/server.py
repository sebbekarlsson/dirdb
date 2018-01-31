from dirdb.connection import Connection
from threading import Thread
import socket


class Server(Thread):

    def __init__(self, base_dir, host='localhost', port=7768):
        Thread.__init__(self)

        self.killed = False
        self.socket = None
        self.connections = []
        self.base_dir = base_dir
        self.host = host
        self.port = port

    def save_document(self, document):
        pass

    def update_document(self, document_id, document):
        pass

    def delete_document(self, document_id):
        pass

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
