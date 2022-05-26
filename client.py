import socket
import sys
import traceback
from datetime import datetime

args = sys.argv[1:]
host = args[0]
port = int(args[1])
keep_alive_enable = args[2]
server_address = (host, port)
recv_size = 1024
message = ""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    if keep_alive_enable == "true":
        client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    client_socket.connect(server_address)
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] connect to Server")
    try:
        while True:
            message = input(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Send to Server> ")
            client_socket.send(message.encode('utf-8'))
            data = client_socket.recv(recv_size)
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] > {data.decode('utf-8')}")
    except KeyboardInterrupt:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] disconnect")
    except Exception:
        traceback.print_exc()