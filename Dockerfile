# Étape 1 : utiliser une image Java pour builder l'application
FROM maven:3.9.4-eclipse-temurin-21 AS builder

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers Maven
COPY pom.xml .
COPY src ./src

# Compiler l'application (skip tests pour rapidité)
RUN mvn clean package -DskipTests

# Étape 2 : créer l'image finale avec Java uniquement
FROM eclipse-temurin:21-jdk-alpine

# Définir le répertoire de travail
WORKDIR /app

# Copier le jar compilé depuis l'étape builder
COPY --from=builder /app/target/*.jar app.jar

# Exposer le port de l'application
EXPOSE 8080

# Commande pour démarrer l'application
ENTRYPOINT ["java", "-jar", "app.jar"]
