import requests
from bs4 import BeautifulSoup as soup


def get_links(url):
    response = requests.get(url)
    page = response.text
    doc = soup(page, "html.parser")
    links = [element.get("href") for element in doc.find_all("a")]
    return links


links = get_links("http://www.python.org")
for link in links:
    print(link)
