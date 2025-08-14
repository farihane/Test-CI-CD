pipeline {
    agent any

    environment {
        // Nom de l'image Maven + JDK à utiliser
        MAVEN_IMAGE = 'maven:3.9.2-jdk21'
    }

    stages {
        stage('Checkout') {
            steps {
                echo "📥 Clonage du repository depuis GitHub..."
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build with Maven in Docker') {
            steps {
                echo "🔨 Build du projet avec Maven dans Docker..."
                script {
                    docker.image(env.MAVEN_IMAGE).inside('-v ${WORKSPACE}:/app -w /app') {
                        sh 'mvn clean package -DskipTests'
                    }
                }
            }
        }

        stage('Success') {
            steps {
                echo "✅ Build terminé avec succès !"
            }
        }
    }

    post {
        failure {
            echo "❌ Pipeline échoué !"
        }
    }
}
