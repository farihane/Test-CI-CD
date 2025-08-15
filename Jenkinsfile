pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Image Maven/Java EXISTANTE sur Docker Hub
                    def mavenImage = "maven:3.9.6-eclipse-temurin-21"

                    echo "Utilisation de l'image Maven : ${mavenImage}"

                    // Pull de l'image
                    bat "docker pull ${mavenImage}"

                    // Build du projet avec Maven dans Docker
                    bat """
                        docker run --rm ^
                        -v %CD%:/app ^
                        -w /app ^
                        ${mavenImage} mvn clean package -DskipTests
                    """
                }
            }
        }
    }
}
