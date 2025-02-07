import requests

def get_poke_api():
    try:
        url_base = 'https://pokeapi.co/api/v2/pokemon/1'
        header = {
            'Content-Type': 'application/json'
        }
        response = requests.get(url_base, headers=header)
        if response.status_code == 200:
            print("recibir")
            data = response.json()
            print(data["abilities"][0])
        else:
            print(
                f"Error al recibir los datos de la API. Código de estado:"
                f"{response.status_code}")
        return response.json()
    except Exception as e:
        print(f'Error al recibir datos de la API: {e}')
        return []

get_poke_api()