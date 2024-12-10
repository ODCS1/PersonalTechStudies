FROM jdk:21-slim

WORKDIR /app

COPY target/account-0.0.1-SNAPSHOT.jar /app/account.jar

ENTRYPOINT [ "java", "-jar", "account.jar" ]