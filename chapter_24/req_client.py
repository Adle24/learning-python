import webbrowser
import requests


print("let's find an old website")

site = input("type a website url: ")
era = input("type a year, month, and day, like 20250714: ") + "0000"
url = f"http://archive.org/wayback/available?url={site}&timestamp={era}"

response = requests.get(url)
data = response.json()

try:
    old_site = data["archived_snapshots"]["closest"]["url"]
    print(f"found this copy: {old_site}")
    webbrowser.open(old_site)
except KeyError:
    print("couldn't find this copy")
