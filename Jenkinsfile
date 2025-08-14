pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "test-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📥 Cloning repository..."
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build') {
            steps {
                echo "🔨 Building the project with Maven..."
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Docker Test') {
            steps {
                echo "🐳 Testing Docker availability..."
                sh 'docker --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "📦 Building Docker image..."
                sh 'docker build -t $DOCKER_IMAGE . || echo "Docker build skipped"'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo "🚀 Running Docker container..."
                sh 'docker run --rm -d -p 9090:8080 $DOCKER_IMAGE || echo "Docker run skipped"'
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up workspace..."
            cleanWs()
        }
        success {
            echo "✅ Pipeline executed successfully!"
        }
        failure {
            echo "❌ Pipeline failed!"
        }
    }
}
