import csv
def guardar_csv(nombre_archivo, latitud, longitud):
    """Se guardan datos enviados por módulo GPS en un archivo csv.

    :param nombre_archivo: Nombre de archivo a escribir
    :type nombre_archivo: string
    :param latitud: Dato de latitud de posición
    :type latitud: string
    :param longitud: Dato de longitud de posición
    :type longitud: string
    """
    # Modo 'a' para agregar datos sin sobrescribir
    with open(nombre_archivo, mode='a', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        # Escribir la fila con latitud y longitud
        escritor_csv.writerow([latitud, longitud])


def guardar_txt(nombre_archivo, latitud, longitud, save_count):
    """Se guardan datos enviados por módulo GPS en un archivo txt.

    :param nombre_archivo: Nombre de archivo a escribir
    :type nombre_archivo: string
    :param latitud: Dato de latitud de posición
    :type latitud: string
    :param longitud: Dato de longitud de posición
    :type longitud: string
    :param save_count: Número de cuenta
    :type save_count: int
    """
    # Modo 'a' para agregar datos sin sobrescribir
    with open(nombre_archivo, 'a') as txt_file:
        txt_file.write(
            f"{save_count}: Latitud: {latitud}, Longitud: {longitud}\n")

