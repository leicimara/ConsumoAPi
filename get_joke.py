import requests
import json

import requests

def fetch_joke():
    url = 'https://api.chucknorris.io/jokes/random?category=dev'
    headers = {'Accept': 'application/json'}
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        joke_data = response.json()
        joke = joke_data['value']
        return joke
    else:
        return 'Erro ao obter a piada'

if __name__ == '__main__':
    joke = fetch_joke()
    print(joke)


