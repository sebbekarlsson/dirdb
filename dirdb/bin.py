from dirdb.server import Server
from dirdb.client import Client
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--dir", help="The base directory where to store data")
args = parser.parse_args()


def run():
    try:
        server = Server(args.dir if args.dir else '/tmp/dirdb')
        server.setDaemon(True)
        server.start()

        while True:
            server.join(1)
    except KeyboardInterrupt:
        server.killed = True


def run_client():
    try:
        client = Client()
        client.setDaemon(True)
        client.start()

        while True:
            client.join(1)
    except KeyboardInterrupt:
        client.killed = True
