from elasticsearch import Elasticsearch
from elasticsearch.exceptions import RequestError
import json

json_file_path = 'data/output.json'
es_client = Elasticsearch(
    [
        {
            'host': 'localhost',
            'port': 9200,
            'scheme': 'http'
        }
    ]
)
index_name = "doga"
mapping = {
    "mappings": {
        "properties": {
            "id": {"type": "text"},
            "document_number": {"type": "text"},
            "document_page": {"type": "text"},
            "document_url": {"type": "text"},
            "publication_day": {"type": "text"},
            "publication_month": {"type": "text"},
            "publication_year": {"type": "text"},
            "announcement_section": {"type": "text"},
            "announcement_subsection": {"type": "text"},
            "announcement_issuer": {"type": "text"},
            "announcement_summary": {"type": "text"},
            "announcement_content": {"type": "text"}

        }
    }
}

if not es_client.indices.exists(index=index_name):
    try:
        # Crea el índice si no existe
        es_client.indices.create(index=index_name)
        print(f"El índice '{index_name}' se ha creado con éxito.")
    except RequestError as e:
        print(f"Error al crear el índice: {e}")
else:
    print(f"El índice '{index_name}' ya existe.")

# print("@@@@@@", es_client.info())
with open(json_file_path, "r", encoding="iso-8859-1") as json_file:
    # Load the JSON data into a Python dictionary or list
    data = json.load(json_file)



for item in data:
    try:
        es_client.index(index=index_name, document=item)
        print(f"Documento de la página {item['document_page']} agregado con éxito.")
    except RequestError as e:
        print(f"Error al agregar documento: {e}")
