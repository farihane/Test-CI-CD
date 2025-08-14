pipeline {
    agent any

    environment {
        // Définir ici les variables globales si nécessaire
        PROJECT_NAME = 'Test-CI-CD'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build with Maven') {
            steps {
                echo '🔨 Building the project with Maven...'
                bat 'mvn clean package -DskipTests'
            }
        }

        stage('Docker Build & Run (Optional)') {
            steps {
                script {
                    try {
                        // Vérifie si Docker est disponible
                        bat 'docker --version'
                        echo '🐳 Docker is available, building image...'
                        bat 'docker build -t test-image .'
                        bat 'docker run --rm test-image'
                    } catch (Exception e) {
                        echo '⚠️ Docker not found, skipping Docker steps.'
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline finished successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
