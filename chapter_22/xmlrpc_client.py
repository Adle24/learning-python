import xmlrpc.client


proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:6789")
num = 7
result = proxy.double(num)
print(result)
