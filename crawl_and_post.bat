@echo off
python -m venv venv
call .\venv\Scripts\activate
python ./define_start_urls.py
echo The crawling process can take a long time. You can reduce the waiting time by removing lines of URLs from the files ./data/XXX_start_urls.json
pause  
scrapy crawl doga_spider
move .\data\TMP_output.json .\data\DOGA_output.json
scrapy crawl boe_spider
move .\data\TMP_output.json .\data\BOE_output.json
echo Elasticsearch must be running on port 9200!!!
pause 
python bulk_post_documents.py


