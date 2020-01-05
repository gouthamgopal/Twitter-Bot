FROM python:3.7-alpine

COPY bots/auth.py /bots/
COPY bots/config.py /bots/
COPY bots/retweet.py /bots/
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

WORKDIR /bots
CMD ["python3", "retweet.py"]