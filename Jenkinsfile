pipeline {
    agent any

    environment {
        // dossier workspace partagé pour Docker Maven
        WORKSPACE_DIR = "${env.WORKSPACE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build with Maven in Docker') {
            steps {
                script {
                    // Utiliser l'image Maven officielle avec JDK
                    docker.image('maven:3.9.4-eclipse-temurin-21').inside("-v ${WORKSPACE_DIR}:${WORKSPACE_DIR}") {
                        sh "cd ${WORKSPACE_DIR} && mvn clean package -DskipTests"
                    }
                }
            }
        }

        stage('Docker Build & Run App') {
            steps {
                script {
                    // Construire l'image Docker de l'application
                    docker.build("springboot-app:${env.BUILD_NUMBER}", "${WORKSPACE_DIR}")
                    // Optionnel : lancer le conteneur
                    // docker.image("springboot-app:${env.BUILD_NUMBER}").run('-p 8080:8080')
                }
            }
        }
    }

    post {
        success { echo '✅ Pipeline terminé avec succès !' }
        failure { echo '❌ Pipeline échoué !' }
    }
}
