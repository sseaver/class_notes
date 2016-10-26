import requests


def get_data(endpoint, lookup="name"):
    url = "http://swapi.co/api/{}/".format(endpoint)
    while url:
        result = requests.get(url)
        json_result = result.json()

        for person in json_result["results"]:
            print(person[lookup])

        if input("Press Enter to keep going, type n to stop"):
            break

        url = json_result["next"]

while True:
    value = input("What do you want to search for? (films) or (people)")
    get_data(value)
