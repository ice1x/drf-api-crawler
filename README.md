# drf-api-crawler
DRF API with Scrapy Crawler

# Kludge for VE's IP hardcode
1. clone this repo
2. enter repo folder
3. `sudo docker-compose build`
4. `sudo docker-compose up`
5. `sudo docker inspect -f '{{.Name}} - {{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' $(sudo docker ps -aq)`
6. get IP of VE with name drf-api-crawler_db_1
7. put this IP to both: `drf-api/settings.py` >> near `DATABASES` >> `HOSTS`
8. and `scrapy_example/pipelines.py` >> near `self.hostname`
9. as well IP of VE drf-api-crawler_db_1 to the `drf-api/settings.py` >> `ALLOWED_HOSTS`
10. `sudo docker-compose down`
11. `sudo docker-compose up`
12. open last IP:8000/posts

# Run crawler manually
* `sudo docker-compose exec drf-api-crawler scrapy crawl forward`
