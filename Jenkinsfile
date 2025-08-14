pipeline {
    agent any

    environment {
        // Nom de l'image Maven avec JDK 21
        MAVEN_IMAGE = 'maven:3.9.2-eclipse-temurin-21'
    }

    stages {

        stage('Checkout') {
            steps {
                echo "📥 Cloning repository..."
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build with Docker Maven') {
            steps {
                echo "🔨 Building project inside Docker container..."
                script {
                    // Exécuter Maven dans Docker
                    def mvnCommand = "mvn clean package -DskipTests"
                    bat """
                    docker run --rm -v "%CD%":/app -w /app ${MAVEN_IMAGE} ${mvnCommand}
                    """
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
