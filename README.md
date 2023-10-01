# DOGa search

## Setup

Create a Virtual Environment
```bash
python -m venv dogaenv # On Mac/Linux use Python3
```

Activate your Virtual Environment
```bash
dogaenv\Scripts\activate # On Windows
source dogaenv/bin/activate # On Mac/Linux
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

## Execution

Copy the desired URLs inside doga_spider.py start_urls variable. To execute the crawler run the following command:
```bash
scrapy crawl doga_spider
```
After its execution, you could find the file "data/"output.json" containing a dictionary of elements

Execute Elastic Search container
```bash
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0
# docker pull docker.elastic.co/elasticsearch/elasticsearch:8.10.1
```

Start webapp

```bash
cd webapp
npm run start
```

## Try it
visit [http://localhost:4200](http://localhost:4200)



TODO: añadir keywoords parsear SL, SLU para obtener empresas, Utiilizar una tabla de Localidades, en oposiciones y nombrameientos sacar Trabajos 
