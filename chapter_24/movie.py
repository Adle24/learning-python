import webbrowser
import requests


def search(title):
    search_url = "https://archive.org/advancedsearch.php"
    params = {
        "q": f"title:({title}) AND mediatype:(movies)",
        "fl": "identifier,title,description",
        "output": "json",
        "rows": 20,
        "page": 1,
    }

    response = requests.get(search_url, params=params)
    data = response.json()
    docs = [
        (doc["identifier"], doc["title"], doc["description"])
        for doc in data["response"]["docs"]
    ]

    return docs


def choose(docs):
    last = len(docs) - 1

    for num, doc in enumerate(docs):
        print(f"{num}: ({doc[1]}) {doc[2][:30]}...")

    index = input(f"Which would you like to see (0 to {last})? ")

    try:
        return docs[int(index)][0]
    except IndexError:
        return None


def display(identifier):
    details_url = f"https://archive.org/details/{identifier}"
    webbrowser.open(details_url)


def main(title):
    identifiers = search(title)

    if identifiers:
        identifier = choose(identifiers)
        if identifier:
            display(identifier)
        else:
            print("nothing selected")
    else:
        print(f"nothing found: {title}")


main("eegah")
