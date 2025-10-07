from datetime import datetime
import socket


server_address = ("127.0.0.1", 6789)
max_size = 4096

print(f"starting server at {datetime.now()}")
print("waiting for a client to call")

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

data, client = server.recvfrom(max_size)

print(f"at {datetime.now()}, {client} said: {data}")
server.sendto(b"Are you talking to me?", client)
server.close()
