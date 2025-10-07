import socket
from datetime import datetime
import zmq
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client


# exercise 1

# client
address = ("localhost", 6789)
max_size = 1000

curent_date = datetime.now()
bytes_current_date = bytes(curent_date.isoformat(), encoding="utf-8")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(address)
client.sendall(bytes_current_date)
client.close()

# server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(address)
server.listen(5)
data = server.recv(max_size)
decoded = data.decode("utf-8")
print(data)
server.close()

# exercise 2

# client
host = "127.0.0.1"
port = 6789

context = zmq.Context()
client = context.socket(zmq.REQ)
client.connect(f"tcp://{host}:{port}")

request_str = datetime.now().isoformat()
request_bytes = request_str.encode("utf-8")
client.send(request_bytes)
print(f"sent {request_str}")

# server
context = zmq.Context()
server = context.socket(zmq.REP)
server.bind(f"tcp://{host}:{port}")

request_bytes = server.recv()
request_str = request_bytes.decode("utf-8")
print(f"that voice in my head says: {request_str}")

# exercise 3


# server
def get_current_time():
    return datetime.now().isoformat()


server = SimpleXMLRPCServer(("localhost", 6789))
server.register_function(get_current_time, "get_current_time")
server.serve_forever()

# client
proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:6789")
result = proxy.get_current_time()
print(result)
