# Этап сборки
FROM maven:3.9.9 AS build

WORKDIR /app

COPY ./ ./

RUN mvn clean package -DskipTests -U

FROM openjdk:17-jdk-slim

WORKDIR /app

# Копируем готовый JAR файл из предыдущего этапа сборки
COPY --from=build /app/target/MusicBot-Snapshot.jar /app/musicbot.jar
COPY ./src/main/resources/reference.conf /app/config.txt

# Открываем порт 8080
EXPOSE 8080

# Команда для запуска приложения
CMD ["java", "-jar", "musicbot.jar"]
