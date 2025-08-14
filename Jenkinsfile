pipeline {
    agent any

    environment {
        // Nom de l'image Docker finale
        IMAGE_NAME = "springboot-app:latest"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Récupération du code depuis GitHub...'
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Detect Java Version') {
            steps {
                script {
                    // Lire la version Java depuis le pom.xml
                    javaVersion = sh(script: "mvn help:evaluate -Dexpression=maven.compiler.source -q -DforceStdout", returnStdout: true).trim()
                    echo "🔍 Version Java détectée : ${javaVersion}"
                }
            }
        }

        stage('Build with Maven in Docker') {
            steps {
                script {
                    echo "🔨 Build Maven dans Docker avec Java ${javaVersion}..."
                    docker.image("maven:3.9.2-jdk${javaVersion}").inside {
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
            echo "❌ Pipeline échoué. Vérifie les logs !"
        }
    }
}
