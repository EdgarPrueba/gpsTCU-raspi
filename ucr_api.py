import requests
import configparser

config = configparser.ConfigParser()
config.read('pipeline.cfg')
url_base = config['api']['url']

def call_api(extension: str, data: dict, method: str):
    try:
        url = f'{url_base}/{extension}'
        header = {
            'Content-Type': 'application/json'
        }
        mensaje = ''
        if method == 'GET':
            response = requests.get(url, headers=header)
            mensaje = "recibir"

        elif method == 'POST':
            response = requests.post(url, headers=header, json=data)
            mensaje = f"enviar"

        elif method == 'PATCH':
            response = requests.patch(url, headers=header, json=data)
            mensaje = f"actualizar"

        if response.status_code >= 200 & response.status_code < 300:
            print(f"Exito al {mensaje} los datos a la API. Código de estado: {response.status_code}")
        else:
            print(
                f"Error al {mensaje} los datos a la API. Código de estado: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f'Error al {mensaje} datos de la API: {e}')
        return []

def get_data(extension: str):
        return call_api(extension, {}, 'GET')

def post_data(extension: str, data: dict):
        return call_api(extension, data, 'POST')

def patch_data(extension: str, data: dict):
        return call_api(extension, data, 'PATCH')