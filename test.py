import requests


def get_attr(ct_name, api):
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': ct_name,
        'key': api,
        'type': 'tourist_attraction',
    }
    response = requests.get(url, params)
    data = response.json()
    # print(data)
    # if 'results' in data:
    for place in data['results']:
        name = place.get('name')
        rating = place.get('rating')
        addy = place.get('formatted_address')
        print(f"{name}: {rating} stars\n{addy}\n")
    else:
        print("No results found.")


if __name__ == "__main__":
    get_attr('Pyongyang', 'AIzaSyBvo0dTu0VrP46PyTW8ORJuCllJxWxF3Wc')
