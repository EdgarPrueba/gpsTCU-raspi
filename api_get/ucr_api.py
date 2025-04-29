import requests
import configparser

config = configparser.ConfigParser()
config.read('pipeline.cfg')
url_base = config['api']['url']


def call_api(extension: str, data: dict, method: str):
    """ Llama a la API de UCR para enviar o recibir datos.

    Esta función realiza una solicitud HTTP (GET, POST, PATCH) a la API utilizando una URL base configurada
    en el archivo de configuración. Dependiendo del método proporcionado, se envían datos o se reciben
    datos de la API.

    :param extension: La extensión que se añade a la URL base para formar la URL completa.
    :type extension: str
    :param data: Los datos a enviar a la API en formato diccionario (solo relevante para POST y PATCH).
    :type data: dict
    :param method: El método HTTP a utilizar. Debe ser uno de los siguientes: 'GET', 'POST', 'PATCH'.
    :type method: str
    :return: La respuesta de la API en formato JSON.
    :rtype: dict
    :raises Exception: Si ocurre un error al hacer la solicitud a la API.
    """
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
            mensaje = "enviar"

        elif method == 'PATCH':
            response = requests.patch(url, headers=header, json=data)
            mensaje = "actualizar"

        if response.status_code >= 200 & response.status_code < 300:
            print(f"Exito al {mensaje} los datos a la API."
                  f"Código de estado: {response.status_code}")
        else:
            print(
                f"Error al {mensaje} los datos a la API."
                f"Código de estado: {response.status_code}")
        return response.json()
    except Exception as e:
        print(f'Error al {mensaje} datos de la API: {e}')
        return []


def get_data(extension: str):
    """ Obtiene datos de la API utilizando el método GET.

    Esta función es un wrapper para la función `call_api` que realiza una solicitud GET a la API.

    :param extension: La extensión que se añade a la URL base para formar la URL completa.
    :type extension: str
    :return: La respuesta de la API en formato JSON.
    :rtype: dict
    """
    return call_api(extension, {}, 'GET')


def post_data(extension: str, data: dict):
    """ Envía datos a la API utilizando el método POST.

    Esta función es un wrapper para la función `call_api` que realiza una solicitud POST a la API.

    :param extension: La extensión que se añade a la URL base para formar la URL completa.
    :type extension: str
    :param data: Los datos a enviar a la API.
    :type data: dict
    :return: La respuesta de la API en formato JSON.
    :rtype: dict
    """
    return call_api(extension, data, 'POST')


def patch_data(extension: str, data: dict):
    """ Actualiza datos en la API utilizando el método PATCH.

    Esta función es un wrapper para la función `call_api` que realiza una solicitud PATCH a la API.

    :param extension: La extensión que se añade a la URL base para formar la URL completa.
    :type extension: str
    :param data: Los datos a enviar a la API.
    :type data: dict
    :return: La respuesta de la API en formato JSON.
    :rtype: dict
    """
    return call_api(extension, data, 'PATCH')
