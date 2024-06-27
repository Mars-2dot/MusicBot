FROM openjdk:11-alpine

WORKDIR /app

COPY ./target/MusicBot-Snapshot.jar /app/musicbot.jar
COPY ./src/main/resources/reference.conf /app/config.txt


EXPOSE 8080

CMD ["java", "-jar", "musicbot.jar"]
