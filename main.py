import os
import sys
import threading
import time
from dotenv import load_dotenv
from src.server.server import run_server
from src.client.client import run_client

load_dotenv()

SERVERIP:str = os.getenv("SERVERIP")
PORT:int = os.getenv("PORT")


def main() -> None:
    if (len(sys.argv) < 2):
        print("usage: python main.py [server|client]")
        return

    mode: str = sys.argv[1].lower()
    print(f"starting mode {mode}")

    if (mode == "server"):
        run_server(port=int(PORT))
    elif (mode == "client"):
        run_client(SERVERIP, int(PORT))
    else:
        print("usage: python main.py [server|client]")
        return

if (__name__ == "__main__"):
    main()