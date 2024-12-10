FROM openjdk:21-slim

WORKDIR /app

COPY target/account-1.0.0-SNAPSHOT.jar /app/account.jar

ENTRYPOINT ["java", "-jar", "account.jar"]