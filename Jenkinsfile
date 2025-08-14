// Jenkinsfile pour un projet Spring Boot + Docker
// Chaque étape est commentée pour bien comprendre le pipeline

pipeline {
    // Définition de l'agent : où la pipeline va s'exécuter
    // Ici, on utilise un container Docker Maven officiel avec Java 21
    agent {
        docker {
            image 'maven:3.9.4-eclipse-temurin-21'
            // Partage du cache Maven pour accélérer les builds
            args '-v /root/.m2:/root/.m2 -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    // Définition des différentes étapes du pipeline
    stages {

        // Étape 1 : Checkout du code depuis GitHub
        stage('Checkout') {
            steps {
                echo "Récupération du code source depuis GitHub..."
                checkout scm // Récupère le code depuis le dépôt configuré dans Jenkins
            }
        }

        // Étape 2 : Build Maven
        stage('Build') {
            steps {
                echo "Compilation du projet Spring Boot avec Maven..."
                sh 'mvn clean package -DskipTests'
                // -DskipTests permet de compiler rapidement sans exécuter les tests
            }
        }

        // Étape 3 : Tests unitaires
        stage('Test') {
            steps {
                echo "Exécution des tests unitaires..."
                sh 'mvn test'
            }
        }

        // Étape 4 : Build de l'image Docker
        stage('Build Docker Image') {
            steps {
                echo "Création de l'image Docker de l'application..."
                sh 'docker build -t springboot-cicd-demo .'
            }
        }

        // Étape 5 : Lancer le container Docker pour vérifier que l'application fonctionne
        stage('Run Docker Container') {
            steps {
                echo "Lancement du container Docker pour vérification..."
                // Stop et supprime un éventuel container existant
                sh 'docker rm -f springboot-cicd-demo || true'
                // Lance le container sur le port 8080
                sh 'docker run -d --name springboot-cicd-demo -p 8080:8080 springboot-cicd-demo'
            }
        }

    }

    // Bloc post pour nettoyer ou notifier
    post {
        always {
            echo "Pipeline terminée."
        }
        success {
            echo "Pipeline réussie !"
        }
        failure {
            echo "Pipeline échouée, vérifier les logs."
        }
    }
}
