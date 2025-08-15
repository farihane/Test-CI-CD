pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build with Docker Maven') {
            steps {
                script {
                    // Détection de la version Java depuis pom.xml directement dans le conteneur
                    def javaVersion = bat(
                        script: 'docker run --rm -v %CD%:/app -w /app maven:3.9.2-eclipse-temurin-21 mvn help:evaluate -Dexpression=java.version -q -DforceStdout',
                        returnStdout: true
                    ).trim()

                    if (!javaVersion) { javaVersion = "21" }

                    def mavenImage = "maven:3.9.2-eclipse-temurin-${javaVersion}"
                    echo "Java détecté : ${javaVersion}"
                    echo "Image Maven : ${mavenImage}"

                    bat "docker pull ${mavenImage}"
                    bat "docker run --rm -v %CD%:/app -w /app ${mavenImage} mvn clean package -DskipTests"
                }
            }
        }
    }
}
