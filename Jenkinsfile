pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Image Maven/Java fonctionnelle
                    def mavenImage = "maven:3.9.6-eclipse-temurin-21"
                    echo "Utilisation de l'image Maven : ${mavenImage}"

                    // Pull de l'image Docker
                    bat "docker pull ${mavenImage}"

                    // Build du projet Maven dans Docker
                    bat """
                        docker run --rm ^
                        -v %CD%:/app ^
                        -w /app ^
                        ${mavenImage} mvn clean package -DskipTests
                    """
                }
            }
        }

        stage('Archive JAR') {
            steps {
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
        }

        stage('Run Application (Optional)') {
            steps {
                script {
                    echo "Test de l'application dans Docker sur le port 8080"
                    bat """
                        docker run --rm -d -p 8080:8080 ^
                        -v %CD%/target:/app maven:3.9.6-eclipse-temurin-21 ^
                        java -jar /app/backend-cicd-demo-0.0.1-SNAPSHOT.jar
                    """
                }
            }
        }
    }

    post {
        success {
            echo "✅ Build terminé avec succès !"
        }
        failure {
            echo "❌ Build échoué"
        }
    }
}
