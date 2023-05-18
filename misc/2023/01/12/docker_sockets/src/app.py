import argparse

from socketer import Socketer
from client import Client
from server import Server

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-t",
        "--type",
        default="client",
    )

    args = parser.parse_args()
    app: Socketer | None = None
    if args.type == "client":
        app = Client()
    elif args.type == "server":
        app = Server()
    else:
        raise KeyError
    app.run()
