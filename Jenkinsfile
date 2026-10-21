pipeline {
    agent any

    environment {
        IMAGE_NAME = 'student-management-cicd'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Test Dependencies') {
            steps {
                bat 'py -m pip install --user -r requirements-dev.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'py -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%BUILD_NUMBER% .'
                bat 'docker tag %IMAGE_NAME%:%BUILD_NUMBER% %IMAGE_NAME%:latest'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f kubernetes/deployment.yaml'
                bat 'kubectl apply -f kubernetes/service.yaml'
                bat 'kubectl rollout status deployment/student-management --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed: tests passed, image built, and Kubernetes deployment updated.'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs above to identify the issue.'
        }
    }
}
