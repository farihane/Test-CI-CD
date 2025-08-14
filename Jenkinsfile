pipeline {
    agent any

    environment {
        MAVEN_IMAGE = 'maven:3.9.2-eclipse-temurin-21'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📥 Cloning repository..."
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }


            }
        }

        stage('Success') {
            steps {
                echo "✅ Build finished successfully!"
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline échoué !"
        }
    }
}
