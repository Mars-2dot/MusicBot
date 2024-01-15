FROM ubuntu:latest

MAINTAINER Mars-2dot

LABEL version="0.9.0"

RUN apt-get update && \
  apt-get install -y python3 python3-pip && \
    apt-get install -y ffmpeg

RUN python3 -m pip install -U discord.py
RUN python3 -m pip install -U yt-dlp pynacl environs pyOpenSSL ndg-httpsclient  pyasn1
COPY ./cogs/* /home/bot/cogs/
COPY ./exception/* /home/bot/exception/
COPY ./exception/errors/* /home/bot/exception/errors/
COPY ./logic/* /home/bot/logic/
COPY ./settings/* /home/bot/settings/
COPY ./main.py /home/bot/

WORKDIR /home/bot

ENTRYPOINT ["/usr/bin/python3", "main.py", "prod"]
