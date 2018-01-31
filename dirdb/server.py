from threading import Thread


class Server(Thread):

    def __init__(self, base_dir):
        Thread.__init__(self)

        self.killed = False
        self.base_dir = base_dir

    def run(self):
        # open socket and start accepting connections
        while not self.killed:
            print('running')
