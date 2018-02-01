from dirdb.connection import Connection
from threading import Thread
import socket
import os
import json


class Server(Thread):

    def __init__(self, base_dir, host='localhost', port=7768):
        Thread.__init__(self)

        self.killed = False
        self.socket = None
        self.connections = []
        self.base_dir = base_dir
        self.host = host
        self.port = port

    def db_exists(self, db):
        return os.path.isdir(os.path.join(self.base_dir, db))

    def create_db(self, db):
        return os.path.mkdir(os.path.join(self.base_dir, db))

    def save_document(self, db, name, document):
        if not self.db_exists(db):
            self.create_db(db)

        filepath = os.path.join(self.base_dir, db, name + '.json')

        filecontents = ''
        with open(filepath) as _file:
            filecontents = _file.read()
        _file.close()

        filecontents = '[]' if not filecontents else filecontents

        data = json.loads(filecontents)

        data.append(document)

        with open(filepath) as _file:
            _file.write(json.dumps(data))
        _file.close()

    def update_document(self, db, query, document):
        current = self.find_document(query)
        print(current)

    def delete_document(self, db, query):
        current = self.find_document(query)
        print(current)

    def find_document(self, db, query):
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
