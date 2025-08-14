pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "springboot-app"
        MAVEN_IMAGE = "maven:3.9.4-eclipse-temurin-21"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📥 Cloning repository..."
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build with Maven in Docker') {
            steps {
                echo "🔨 Building with Maven inside Docker..."
                sh """
                    docker run --rm \
                        -v \$PWD:/app \
                        -w /app \
                        ${MAVEN_IMAGE} mvn clean package -DskipTests
                """
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "🐳 Building Docker image..."
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "🚀 Running application container..."
                sh """
                    docker rm -f ${DOCKER_IMAGE} || true
                    docker run -d --name ${DOCKER_IMAGE} -p 8080:8080 ${DOCKER_IMAGE}
                """
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
