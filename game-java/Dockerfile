FROM openjdk:17-alpine

LABEL version="1.0.1"
LABEL description="Java Guessing Game"
WORKDIR /app

COPY game.java .

RUN javac game.java

CMD ["java", "game"]

