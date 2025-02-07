import json

with open("src/prueba_paradas.json") as paradas:
    datos = json.load(paradas)

    # print(datos)
    print("\tDireccion\tLlegada")
    for bus in datos["buses_por_llegar"]:
        print(f"\t{bus['Direccion']}\t{bus['llegada']}")