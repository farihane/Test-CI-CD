pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    docker.image('maven:3.9.4-eclipse-temurin-21').inside {
                        sh 'mvn clean package -DskipTests'
                    }
                }
            }
        }
    }
}
