from threading import Thread


class Connection(Thread):

    def __init__(self, socket, server):
        Thread.__init__(self)

        self.socket = socket
        self.server = server

    def run(self):
        # start reading incoming data from socket
        pass
