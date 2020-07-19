FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN git clone https://github.com/ice1x/drf-api-crawler.git /code/
WORKDIR /code/
RUN pip install --upgrade incremental
RUN pip install -r requirements.txt
