pipeline {
    agent any

    environment {
        IMAGE_NAME = "springboot-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Récupération du code depuis GitHub...'
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build & Package in Docker') {
            steps {
                script {
                    echo "🔨 Build Maven dans Docker..."
                    // Tout se fait dans le conteneur Maven, pas besoin de Java/Maven sur Jenkins
                    docker.image('maven:3.9.2-jdk21').inside {
                        sh 'mvn clean package -DskipTests'
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "🐳 Création de l'image Docker..."
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run App') {
            steps {
                script {
                    echo "🚀 Lancement de l'application dans Docker..."
                    // Supprime le conteneur existant si présent
                    sh "docker rm -f springboot-app || true"
                    sh "docker run -d -p 8080:8080 --name springboot-app ${IMAGE_NAME}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline terminé avec succès !"
        }
        failure {
            echo "❌ Pipeline échoué, vérifie les logs !"
        }
    }
}
