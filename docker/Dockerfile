FROM python:3.7
MAINTAINER Andrew Smirnov <smirnov@informatics.ru>
ADD ./ /yet_another_calculator
WORKDIR /yet_another_calculator/
CMD exec apt-get update
CMD exec apt-get install python3-dev libmysqlclient-dev build-essential nano
RUN pip install --no-cache-dir -r ./requirements.txt
CMD exec ./docker/run.sh
