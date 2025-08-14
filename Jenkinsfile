pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Cloning repository...'
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build') {
            steps {
                echo '🔨 Building the project with Maven...'
                bat 'mvn clean package -DskipTests'
            }
        }
    }

    post {
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
