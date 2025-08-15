pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build Maven & Package') {
            steps {
                script {
                    def mavenImage = "maven:3.9.6-eclipse-temurin-21"
                    bat "docker pull ${mavenImage}"
                    bat """
                        docker run --rm ^
                        -v %CD%:/app ^
                        -w /app ^
                        ${mavenImage} mvn clean package -DskipTests
                    """
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def imageName = "springboot-demo:latest"
                    bat "docker build -t ${imageName} ."
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    def containerName = "springboot-demo-container"
                    bat "docker rm -f ${containerName} || exit 0"
                    bat "docker run -d -p 8081:8080 --name ${containerName} springboot-demo:latest"
                }
            }
        }
    }

}
