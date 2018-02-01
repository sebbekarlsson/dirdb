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

        if not os.path.isdir(self.base_dir):
            os.mkdir(self.base_dir)

    def db_exists(self, db):
        return os.path.isdir(os.path.join(self.base_dir, db))

    def create_db(self, db):
        return os.mkdir(os.path.join(self.base_dir, db))

    def save_document(self, db, name, document):
        if not self.db_exists(db):
            self.create_db(db)

        filepath = os.path.join(self.base_dir, db, name + '.json')

        if not os.path.isfile(filepath):
            with open(filepath, 'w+') as _file:
                _file.write('')
            _file.close()

        filecontents = ''
        with open(filepath) as _file:
            filecontents = _file.read()
        _file.close()

        filecontents = '[]' if not filecontents else filecontents

        data = json.loads(filecontents)

        data.append(document)

        with open(filepath, 'w+') as _file:
            _file.write(json.dumps(data))
        _file.close()

    def update_document(self, db, query, document):
        current = self.find_document(query)
        print(current)

    def delete_document(self, db, query):
        current = self.find_document(query)
        print(current)

    def find_document(self, db, query):
        filepath = os.path.join(self.base_dir, db, query['$name'] + '.json')

        contents = ''
        with open(filepath, 'r+') as _file:
            contents = _file.read()
        _file.close()
        contents = '[]' if not contents else contents

        return json.loads(contents)

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
