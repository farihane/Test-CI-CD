pipeline {
    agent any

    environment {
        // Valeurs par défaut
        MAVEN_IMAGE = ''
        JAVA_VERSION = ''
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Detect Java from pom.xml') {
            steps {
                script {
                    // Récupérer la version Java depuis le pom.xml
                    JAVA_VERSION = bat(
                        script: 'mvn help:evaluate -Dexpression=java.version -q -DforceStdout',
                        returnStdout: true
                    ).trim()

                    if (!JAVA_VERSION) {
                        JAVA_VERSION = "21" // fallback par défaut
                    }

                    echo "✅ Java version détectée : ${JAVA_VERSION}"

                    // Mapping version -> image Maven Docker
                    def mavenImageMap = [
                        "21": "maven:3.9.2-eclipse-temurin-21",
                        "17": "maven:3.9.2-eclipse-temurin-17",
                        "11": "maven:3.9.2-eclipse-temurin-11"
                    ]

                    MAVEN_IMAGE = mavenImageMap.get(JAVA_VERSION, "maven:3.9.2-eclipse-temurin-21")
                    env.MAVEN_IMAGE = MAVEN_IMAGE

                    echo "🚀 Image Maven sélectionnée : ${MAVEN_IMAGE}"
                }
            }
        }

        stage('Pull Maven image') {
            steps {
                bat "docker pull ${MAVEN_IMAGE}"
            }
        }

        stage('Build (Dockerized Maven)') {
            steps {
                bat """
                docker run --rm -v %CD%:/app -w /app ${MAVEN_IMAGE} mvn clean package -DskipTests
                """
            }
        }

        stage('Archive JAR') {
            steps {
                archiveArtifacts artifacts: '**/target/*.jar', fingerprint: true
            }
        }

        stage('Docker Build App (optional)') {
            when {
                expression { fileExists('Dockerfile') }
            }
            steps {
                bat "docker build -t myapp:latest ."
            }
        }
    }

    post {
        always {
            echo "🧹 Fin du pipeline"
        }
        failure {
            echo "❌ Build échoué"
        }
        success {
            echo "✅ Build réussi"
        }
    }
}
