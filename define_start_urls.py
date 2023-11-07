from datetime import datetime, timedelta
import json


def save_file(file, content):
    try:
        # Open the JSON file in write mode and save the data
        with open(file, 'w') as json_file:
            json.dump(content, json_file, indent=4)  # indent for pretty formatting (optional)
        print(f"Data saved to '{file}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


def define_start_urls():
    date = datetime.now()
    DOGA_start_urls = []
    BOE_start_urls = []

    # Genero todas las fechas de este año hasta hoy
    while date.year == datetime.now().year:
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        date -= timedelta(days=1)
        # Almaceno las entradas de las publicaciones para esas fechas
        DOGA_start_urls.append(f'https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/{year}/{year}{month}{day}/Secciones1_gl.html')
        BOE_start_urls.append(f'https://www.boe.es/boe/dias/{year}/{month}/{day}/')
    # Las salvo a disco
    save_file('data/DOGA_start_urls.json', {"urls": DOGA_start_urls})
    save_file('data/BOE_start_urls.json', {"urls": BOE_start_urls})


define_start_urls()
