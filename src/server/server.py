import socket

ip= '0.0.0.0'

def run_server(port:int = 8080) -> None:
    print(f"start server at {ip}:{port}", flush=True)
    try:
        while True:
            server = socket.socket()
            server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            server.bind((ip, port))
            server.listen(5)
            # print(f"wating on {ip}:{port}", flush=True)

            client,addr = server.accept()
            data = client.recv(1024).decode('utf-8')
            print(f"{client} send {data}", flush=True)
            client.close()
    except Exception as e:
        print(f"error -> {e}", flush=True)
