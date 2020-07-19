FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN apt-get install -y cron
RUN git clone https://github.com/ice1x/drf-api-crawler.git /code/
WORKDIR /code/
RUN pip install --upgrade incremental
RUN pip install -r requirements.txt
ADD crontabfile /code/
RUN crontab /code/crontabfile
CMD ["cron", "-f"]
