# PAP search

## Description
Scrapes public administration publications information and stores it in an ElasticSearch Instance. Currently supports Diario oficial de Galicia (DOGA) publications

## Setup

Create a Virtual Environment
```bash
python -m venv papenv # On Mac/Linux use Python3
```

Activate your Virtual Environment
```bash
papenv\Scripts\activate # On Windows
source papenv/bin/activate # On Mac/Linux
```

Install project dependencies
```bash
pip install -r requirements.txt
```

Get a list of initial pages to configure the crawler. You could use this script to generate pages from the current year.
```bash
python define_start_urls.py # On Mac/Linux use Python3 
```
it will store a bunch of urls inside "data/start_urls.json" to access current year DOGa documents

## Crawl

To execute the crawler run the following command:
```bash
scrapy crawl doga_spider
```
It will crawl the seed url's from "data/DOGA_start_urls.json". After its execution, you could find the file "data/TMP_output.json" containing a dictionary of elements  You'll have to manually rename this file to "data/DOGA_output.json".

## Store data
The options to deploy a development setup are:
1. Execute a Elastic Search container 
```bash
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0
```
2. Run a Elastic search instance
   
   [Download ElasticSearch](https://www.elastic.co/es/downloads/elasticsearch)

   Since version 8 uses https by default, this could be modified editing the configuration file `config/elasticsearch.yml` and adding to the bottom the following directives.
```yml
xpack.security.enabled: false
xpack.security.transport.ssl.enabled: false
xpack.security.http.ssl.enabled: false
```

To store the scrapped documents in ElasticSearch run the command:
```bash
python bulk_post_documents.py # On Mac/Linux use Python3 
```
    
## Run webapp

There's also a client to consume the stored data, check the [PAP Search Client repository](https://github.com/pablomarino/pap-search-client) for instructions of how to execute it !!


scrapy genspider boe_spider boe.es  