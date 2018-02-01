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
                try:
                    self.socket.send(json.dumps({'ok': False, 'msg': 'parse'}))
                except Exception:
                    return

                continue

            if '$name' not in data:
                self.socket.send(json.dumps({'ok': False}))
                continue

            if '$db' not in data:
                self.socket.send(json.dumps({'ok': False}))
                continue

            db = data['$db']
            name = data['$name']

            if '$set' not in data and '$find' not in data:
                # query.type == 'save'

                self.server.save_document(db, name, data)

                self.socket.send(json.dumps({'ok': True}))
            elif '$find' in data:
                objects = self.server.find_document(db, data)
                self.socket.send(json.dumps(objects))

            print(data)
