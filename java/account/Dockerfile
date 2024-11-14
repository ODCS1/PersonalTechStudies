FROM openjdk

WORKDIR /app

COPY target/spring-app-1.0.0-SNAPSHOT.jar /app/spring-app.jar

ENTRYPOINT ["java", "-jar", "spring-app.jar"]