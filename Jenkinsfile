pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git url: 'https://github.com/farihane/Test-CI-CD.git', branch: 'main'
            }
        }

        stage('Build with Maven') {
            steps {
                echo '🔨 Building the project with Maven inside Docker...'
                docker.image('maven:3.9.4-eclipse-temurin-21').inside {
                    sh 'mvn clean package -DskipTests'
                }
            }
        }

        stage('Test Docker') {
            steps {
                echo '🐳 Docker is available for later stages if needed'
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
