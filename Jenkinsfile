pipeline {
    agent any

    stages {
    stage('Call Colab Hello') {
        steps {
            script {
                bat '''
                python - <<END
    import requests

    GENAI_URL = "https://e9d60ad9df77.ngrok-free.app/hello"  # URL ngrok de ton Colab

    response = requests.get(GENAI_URL)
    print("Message from Colab:", response.json())
    END
                '''
            }
        }
    }

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/farihane/Test-CI-CD.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t springboot-demo:latest .'
            }
        }

        stage('Run Application') {
            steps {
                bat 'docker rm -f springboot-demo-container || exit 0'
                bat 'docker run -d -p 8081:8080 --name springboot-demo-container springboot-demo:latest'
            }
        }
    }
}
