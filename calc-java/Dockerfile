FROM openjdk:17-alpine

LABEL version="1.0.1"
LABEL description="Java Calculator"
WORKDIR /app

COPY calc.java .

RUN javac calc.java

CMD ["java", "calc"]

