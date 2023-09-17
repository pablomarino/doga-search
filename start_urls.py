from datetime import datetime,timedelta
def define_start_urls():
    date = datetime.now()
    start_urls = []
    while date.year == datetime.now().year:
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")
        date -= timedelta(days=1)
        start_urls.append(f'https://www.xunta.gal/diario-oficial-galicia/mostrarContenido.do?ruta=/u01/app/oracle/shared/resources/pxdog100/doga/Publicados/{year}/{year}{month}{day}/Secciones1_gl.html')
    print(start_urls)

define_start_urls()