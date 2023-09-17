# DOGa search

# Setup


Install project dependencies
```bash
pip -r requirements.txt
```
Get a list of initial pages to configure the crawler. You could use this script to generate pages from the current year.
```bash
python start_urls.py > urls.txt # On Mac/Linux use Python3 
```
Copy the URLs inside doga_spider.py start_urls variable. To execute the crawler run the following commands:
```bash
cd doga
scrapy crawl doga_spider
```
