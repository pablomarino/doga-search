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

To execute the crawler run the following command:
```bash
scrapy crawl doga_spider
```
It will crawl the seed url's from "data/start_urls.json". After its execution, you could find the file "data/"output.json" containing a dictionary of elements

Execute Elastic Search container 
```bash
docker compose up
```
or run a Elastic search instance

To store scrapped in Elastic shearch the documents run the command:
```bash
python bulk_post_documents.py # On Mac/Linux use Python3 
```

Start webapp

```bash
cd webapp
npm run start
```

## Try it
visit [http://localhost:4200](http://localhost:4200)



TODO: añadir keywoords parsear SL, SLU para obtener empresas, Utiilizar una tabla de Localidades, en oposiciones y nombrameientos sacar Trabajos 
