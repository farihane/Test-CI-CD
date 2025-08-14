pipeline {
    agent {
        docker {
            image 'maven:3.9.4-eclipse-temurin-21' // image Docker officielle Maven + JDK 21
            args '-v /root/.m2:/root/.m2'        // cache Maven local
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package -DskipTests'
            }
        }
    }
}
