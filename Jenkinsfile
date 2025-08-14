pipeline {
    // Utilise n'importe quel agent disponible sur Jenkins
    agent any

    environment {
        // Définir le chemin pour Maven local si nécessaire
        MAVEN_HOME = "/usr/share/maven"
    }

    stages {

        stage('Checkout') {
            steps {
                // Récupérer le code depuis Git
                git url: 'https://github.com/farihane/Test-CI-CD.git', branch: 'main'
            }
        }

        stage('Build') {
            steps {
                echo '🔨 Building the Spring Boot project...'
                // Utilisation de Maven pour compiler et packager le projet
                sh 'mvn clean package -DskipTests'
            }
        }

        stage('Test') {
            steps {
                echo '✅ Running tests...'
                sh 'mvn test'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '🐳 Building Docker image...'
                // Construire l'image Docker du projet Spring Boot
                sh 'docker build -t springboot-cicd-demo .'
            }
        }

        stage('Run Docker Container') {
            steps {
                echo '🚀 Running Docker container...'
                // Supprimer l'ancien container si il existe
                sh 'docker rm -f springboot-cicd-demo || true'
                // Lancer le container sur le port 8081
                sh 'docker run -d -p 8081:8080 --name springboot-cicd-demo springboot-cicd-demo'
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
        success {
            echo '🎉 Build and deployment succeeded!'
        }
        failure {
            echo '❌ Build or deployment failed!'
        }
    }
}
