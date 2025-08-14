pipeline {
    agent any  // utilise le node Jenkins disponible
    environment {
        DOCKER_HOST = 'unix:///var/run/docker.sock' // permet à Jenkins de communiquer avec Docker
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t springboot-cicd-demo .'
            }
        }
        stage('Run Docker Container') {
            steps {
                sh 'docker rm -f springboot-cicd-demo || true'
                sh 'docker run -d --name springboot-cicd-demo -p 8080:8080 springboot-cicd-demo'
            }
        }
    }
}
