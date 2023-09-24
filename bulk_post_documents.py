from elasticsearch import Elasticsearch
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
print("@@@@@@", es_client.info())
with open(json_file_path, "r", encoding="iso-8859-1") as json_file:
    # Load the JSON data into a Python dictionary or list
    data = json.load(json_file)

for item in data:
    resp = es_client.index(index=index_name, document=item)
    print(resp)
