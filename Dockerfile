FROM python:3.8
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
cd /code
RUN git clone git@github.com:ice1x/drf-api-crawler.git
cd ./drf-api-crawler
WORKDIR /code/drf-api-crawler
RUN pip install --upgrade incremental
RUN pip install -r requirements.txt

