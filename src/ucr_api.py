import requests

def call_api(extension: str, data: dict, method: str):
    try:
        url_base = 'https://realtime.bucr.digital/api'
        url = f'{url_base}/{extension}'
        header = {
            'Content-Type': 'application/json'
        }
        mensaje = ''
        if method == 'GET':
            response = requests.get(url, headers=header)
            mensaje = f"Datos recibidos correctamente a la API."

        elif method == 'POST':
            response = requests.post(url, headers=header, json=data)
            mensaje = f"Datos enviados correctamente a la API."

        elif method == 'PATCH':
            response = requests.patch(url, headers=header, json=data)
            mensaje = f"Datos actualizados correctamente a la API."

        if response.status_code == 200:
            print(mensaje)
        else:
            print(
                f"Error al enviar los datos a la API. Código de estado:"
                f"{response.status_code}")
        return response.json()
    except Exception as e:
        print(f'Error al obtener datos de la API: {e}')
        return []

def get_data(extension: str):
        return call_api(extension, {}, 'GET')

def post_data(extension: str, data: dict):
        return call_api(extension, data, 'POST')

def patch_data(extension: str, data: dict):
        return call_api(extension, data, 'PATCH')