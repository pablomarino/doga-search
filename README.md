# DOGa search

## Setup

Create a Virtual Environment
```bash
python -m venv myenv
```

Activate your Virtual Environment
```bash
venv\Scripts\activate # On Windows
source ./venv/bin/activate # On Mac/Linux
```

Install project dependencies
```bash
pip -r requirements.txt
```

Get a list of initial pages to configure the crawler. You could use this script to generate pages from the current year.
```bash
python start_urls.py > urls.txt # On Mac/Linux use Python3 
```
## Execution

Copy the URLs inside doga_spider.py start_urls variable. To execute the crawler run the following commands:
```bash
cd doga
scrapy crawl doga_spider
```

Execute Elastic Search container
```bash
docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.10.0
# docker pull docker.elastic.co/elasticsearch/elasticsearch:8.10.1
```


