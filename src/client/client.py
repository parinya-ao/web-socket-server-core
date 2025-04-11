import socket


def run_client(serverip: str="192.168.0.106", port : int = 8080) -> None:
    while True:
        data = str(input("message -> "))
        client = socket.socket()
        client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        client.connect((serverip, port))
        client.send(data.encode('utf-8'))
        data_client = client.recv(1024).decode('utf-8')
        #print(f"{client} send {data_client}", flush=True)
        client.close()

if (__name__ == "__main__"):
    run_client()