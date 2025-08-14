pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }
        stage('Build in Docker') {
            steps {
                bat '''
                docker run --rm -v "%CD%":/app -w /app maven:3.9.6-eclipse-temurin-17 mvn clean package -DskipTests
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                bat 'docker build -t springboot-app .'
            }
        }
        stage('Run App') {
            steps {
                bat 'docker run -d -p 8080:8080 springboot-app'
            }
        }
    }
}
