pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'docker build -t backend-cicd-demo:latest .'
            }
        }
        stage('Deploy') {
            steps {
                sh 'kubectl apply -f k8s-deployment.yaml'
            }
        }
    }
}
