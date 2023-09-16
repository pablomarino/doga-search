import datetime

class FechaParser:
    traduccion_dias = {
        "Luns": "Monday",
        "Martes": "Tuesday",
        "Mércores": "Wednesday",
        "Xoves": "Thursday",
        "Venres": "Friday",
        "Sábado": "Saturday",
        "Domingo": "Sunday"
    }

    traduccion_meses = {
        "xaneiro": "January",
        "febreiro": "February",
        "marzo": "March",
        "abril": "April",
        "maio": "May",
        "xuño": "June",
        "xullo": "July",
        "agosto": "August",
        "setembro": "September",
        "outubro": "October",
        "novembro": "November",
        "decembro": "December"
    }

    @classmethod
    def traducir(cls, fecha):
        for dia, traduccion in cls.traduccion_dias.items():
            fecha = fecha.replace(dia, traduccion)
        for mes, traduccion in cls.traduccion_meses.items():
            fecha = fecha.replace(mes, traduccion)
        return fecha

    @classmethod
    def extract(cls, fecha_str):
        # Traducir la fecha al formato en inglés
        fecha_str = cls.traducir(fecha_str)

        # Formatear la fecha en el formato deseado
        fecha_obj = datetime.datetime.strptime(fecha_str, "%A, %d de %B de %Y")
        dia_semana = fecha_obj.strftime("%A")
        dia = fecha_obj.strftime("%d")
        mes = fecha_obj.strftime("%B")
        ano = fecha_obj.strftime("%Y")

        return {
            dia_semana,
            dia,
            mes,
            ano
        }
# Función extrae dia de la semana, dia, mes y año de cadenas de texto de fecha en gallego
# Ejemplo de uso:
# fecha_str = "Venres, 15 de setembro de 2023"
# resultado = FechaParser.extract(fecha_str)
# print(resultado)
