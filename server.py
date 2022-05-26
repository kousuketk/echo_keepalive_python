import socket
import sys
import traceback
from datetime import datetime

args = sys.argv[1:]

host = "0.0.0.0"
port = int(args[0])
keep_alive_enable = args[1]

bind_address = (host, port)
backlog_size = 10
recv_size = 1024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    if keep_alive_enable == "true":
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
    
    server_socket.bind(bind_address)
    server_socket.listen(backlog_size)

    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Server startup")

    try:
        while True:
            client_socket, addr = server_socket.accept()
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] accept client")
            
            while True:
                data = client_socket.recv(recv_size)
                if not data:
                    break
                client_socket.send(b'Reply: ' + data)
                print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] receive / send message")
            
            print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] disconnect client")
    except KeyboardInterrupt:
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Server stop")
    except Exception:
        traceback.print_exc()