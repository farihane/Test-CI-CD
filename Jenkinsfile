pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'maven:3.9.4-eclipse-temurin-21'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git url: 'https://github.com/farihane/Test-CI-CD.git', branch: 'main'
            }
        }

        stage('Build with Maven') {
            steps {
                echo '🔨 Building the project with Maven...'
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Docker Build & Run') {
            steps {
                script {
                    echo '🐳 Building Docker image...'
                    sh 'docker build -t test-app .'

                    echo '▶ Running Docker container...'
                    sh 'docker run --rm -d -p 8081:8080 test-app'
                }
            }
        }

        stage('Test Container') {
            steps {
                echo '✅ Docker container should now be running on port 8081'
            }
        }
    }

    post {
        always {
            echo '🧹 Pipeline finished!'
        }
        success {
            echo '🎉 Pipeline succeeded!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
