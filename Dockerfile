FROM ubuntu:latest

MAINTAINER Mars-2dot

LABEL version="0.9.0"

RUN apt-get update && \
  apt-get install -y python3 python3-pip

RUN pip install discord youtube_dl requests pynacl ytdl yt_dlp

COPY ./cogs/* /home/bot/cogs/
COPY ./exception/* /home/bot/exception/
COPY ./exception/errors/* /home/bot/exception/errors/
COPY ./logic/* /home/bot/logic/
COPY ./settings/* /home/bot/settings/
COPY ./main.py /home/bot/

# Enter token for test
ENV MusicBotTokenTest=""
# Enter token main
ENV MusicBotToken=""

WORKDIR /home/bot

ENTRYPOINT ["/usr/bin/python3", "main.py"]
