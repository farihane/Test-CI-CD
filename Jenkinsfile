pipeline {
    agent {
        docker {
            image 'maven:3.9.4-eclipse-temurin-21'  // conteneur officiel Maven avec Java 21
            args '-v $HOME/.m2:/root/.m2'           // persister le cache Maven entre builds
        }
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building the Spring Boot project...'
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'mvn test'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t springboot-cicd-demo .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo 'Running Docker container...'
                sh 'docker rm -f springboot-cicd-demo || true'
                sh 'docker run -d --name springboot-cicd-demo -p 8080:8080 springboot-cicd-demo'
            }
        }
    }
}
