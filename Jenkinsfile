pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    def imageName = "springboot-demo:latest"
                    echo "Construction de l'image Docker : ${imageName}"

                    // Dockerfile s'occupe de compiler le projet et créer le JAR
                    bat "docker build -t ${imageName} ."
                }
            }
        }

        stage('Run Application') {
            steps {
                script {
                    def containerName = "springboot-demo-container"

                    // Arrêter et supprimer le conteneur existant si présent
                    bat "docker rm -f ${containerName} || exit 0"

                    // Lancer le conteneur
                    bat "docker run -d -p 8081:8080 --name ${containerName} ${imageName}"
                }
            }
        }
    }

    post {
        success {
            echo "✅ Application déployée avec succès dans Docker !"
        }
        failure {
            echo "❌ Build ou déploiement échoué !"
        }
    }
}
