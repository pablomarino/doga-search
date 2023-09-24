from datetime import datetime,timedelta
import json
def define_start_urls():
    date = datetime.now()
    start_urls = []
    while date.year == datetime.now().year:
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        date -= timedelta(days=1)
        start_urls.append(f'https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/{year}/{year}{month}{day}/Secciones1_gl.html')
    # print(start_urls)
    json_file_path = 'data/start_urls.json'
    try:
        # Open the JSON file in write mode and save the data
        with open(json_file_path, 'w') as json_file:
            json.dump(start_urls, json_file, indent=4)  # indent for pretty formatting (optional)

        print(f"Data saved to '{json_file_path}' successfully.")

    except Exception as e:
        print(f"An error occurred: {str(e)}")





define_start_urls()