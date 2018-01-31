from dirdb.server import Server
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="The base directory where to store data")
args = parser.parse_args()


def run():
    try:
        server = Server(args.dir if args.dir else '/tmp/dirdb')

        server.start()

        while True:
            server.join(1)
    except KeyboardInterrupt:
        server.killed = True
