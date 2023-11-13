from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
import json

json_file_path = ['data/DOGA_output.json', 'data/BOE_output.json']
es_client = Elasticsearch(
    [
        {
            'host': 'localhost',
            'port': 9200,
            'scheme': 'http'
        }
    ]
)
index_name = "pap"

mapping = {
        "properties": {
            "publication_id": {
                "type": "text",
            },
            "announcement_content": {
                "type": "text",
            },
            "announcement_issuer": {
                "type": "text",
            },
            "announcement_section": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "announcement_subsection": {
                "type": "text",
            },
            "announcement_summary": {
                "type": "text",
            },
            "document_number": {
                "type": "integer",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "document_page": {
                "type": "integer",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "document_url": {
                "type": "text",
                "fields": {
                    "keyword": {
                        "type": "keyword",
                        "ignore_above": 256
                    }
                }
            },
            "publication_date": {
                "type": "date"
            }
        }
}
total_files = 0
# Creo el indice
if not es_client.indices.exists(index=index_name):
    try:
        # Crea el índice si no existe
        es_client.indices.create(index=index_name, mappings=mapping, ignore=400)
        print(f"El índice '{index_name}' se ha creado con éxito.")
    except RequestError as e:
        print(f"Error al crear el índice: {e}")
else:
    print(f"El índice '{index_name}' ya existe.")

for filename in json_file_path:
    # Cargo el fichero que contiene los documentos
    with open(filename, "r", encoding="utf-8") as json_file:
        # Load the JSON data into a Python dictionary or list
        data = json.load(json_file)

    # Añado los documentos
    for item in data:
        try:
            es_client.index(index=index_name, document=item)
            print(f"{item['publication_id']} - Documento de la página {item['document_page']} agregado con éxito.")
            total_files = total_files + 1
        except RequestError as e:
            print(f"Error al agregar documento: {e}")

print(f"{total_files} documentos añadidos")
