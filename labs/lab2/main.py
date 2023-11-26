import requests
from xml.dom.minidom import parseString
import csv

def get_train_data():
    # URL de la API ferroviaria de Irlanda para obtener datos de trenes en tiempo real
    url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

    # Realizar una solicitud HTTP GET a la URL
    response = requests.get(url)

    # Verificar si la solicitud fue exitosa (código de estado HTTP 200)
    if response.status_code == 200:
        return response.text
    else:
        return None

def parse_and_filter_xml_data(xml_data):
    # Analizar los datos XML obtenidos de la API
    dom = parseString(xml_data)

    # Encontrar todos los elementos 'objTrainPositions' en el documento XML
    trains = dom.getElementsByTagName('objTrainPositions')

    # Filtrar solo aquellos trenes cuyo código de tren comience con "D"
    filtered_trains = []
    for train in trains:
        train_code = train.getElementsByTagName('TrainCode')[0].firstChild.data
        if train_code.startswith("D"):
            train_info = {
                'TrainCode': train_code,
                'TrainDate': train.getElementsByTagName('TrainDate')[0].firstChild.data,
                'TrainLatitude': train.getElementsByTagName('TrainLatitude')[0].firstChild.data,
                'TrainLongitude': train.getElementsByTagName('TrainLongitude')[0].firstChild.data,
                'TrainStatus': train.getElementsByTagName('TrainStatus')[0].firstChild.data,
                'TrainMessage': train.getElementsByTagName('PublicMessage')[0].firstChild.data
            }
            filtered_trains.append(train_info)

    return filtered_trains

def write_to_csv(trains_data):
    # Nombres de las columnas para el archivo CSV
    fieldnames = ['TrainCode', 'TrainDate', 'TrainLatitude', 'TrainLongitude', 'TrainStatus', 'TrainMessage']

    # Crear y escribir en un archivo CSV
    with open('trains_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Escribir la cabecera del CSV
        writer.writeheader()

        # Escribir los datos de cada tren
        for train in trains_data:
            writer.writerow(train)

# Llamadas a las funciones para realizar las tareas
xml_data = get_train_data()
if xml_data:
    trains_data = parse_and_filter_xml_data(xml_data)
    write_to_csv(trains_data)
    print("Los datos de los trenes han sido guardados en 'trains_data.csv'.")
else:
    print("Error al obtener datos de la API.")
