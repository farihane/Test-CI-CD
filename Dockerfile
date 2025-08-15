# Étape 1 : Build avec Maven
FROM maven:3.9.6-eclipse-temurin-21 AS build
WORKDIR /app
COPY pom.xml .
# Optimisation du cache Maven
RUN mvn -B -q -DskipTests dependency:go-offline
COPY src ./src
RUN mvn -B clean package -DskipTests

# Étape 2 : Runtime
FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /app/target/*.jar app.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/app.jar"]
