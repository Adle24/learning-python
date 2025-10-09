import urllib.request as ur


url = "http://www.example.com/"
connection = ur.urlopen(url)
data = connection.read()
decoded_data = data.decode("utf-8")

print(f"status code: {connection.status}")
print(decoded_data)

for k, v in connection.getheaders():
    print(f"{k}: {v}")
