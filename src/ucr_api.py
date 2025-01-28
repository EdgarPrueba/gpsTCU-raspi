import requests

def get_data(extension: str):
    try:
        url_base = 'https://realtime.bucr.digital/api'
        url = f'{url_base}/{extension}'
        header = {
            'Content-Type': 'application/json'
        }
        response = requests.get(url, headers=header)
        return response.json()
    except Exception as e:
        print(f'Error al obtener datos de la API: {e}')
        return []
    
def post_data(extension: str, data: dict):
    try:
        url_base = 'https://realtime.bucr.digital/api'
        url = f'{url_base}/{extension}'
        header = {
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=header, json=data)
        return response.json()
    except Exception as e:
        print(f'Error al enviar datos a la API: {e}')
        return []
    
def patch_data(extension: str, data: dict):
    try:
        url_base = 'https://realtime.bucr.digital/api'
        url = f'{url_base}/{extension}'
        header = {
            'Content-Type': 'application/json'
        }
        response = requests.patch(url, headers=header, json=data)
        return response.json()
    except Exception as e:
        print(f'Error al enviar datos a la API: {e}')
        return []