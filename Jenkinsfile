pipeline {
    agent any

    environment {
        AWS_REGION = "ap-south-1"
        AWS_CREDENTIALS = credentials('aws-credentials')
        FRONTEND_REPO = "617996010987.dkr.ecr.ap-south-1.amazonaws.com/frontend-repo"
        BACKEND_REPO = "617996010987.dkr.ecr.ap-south-1.amazonaws.com/backend-repo"
    }

    stages {

        stage('Clone Code') {
            steps {
                git branch: 'main', url: 'https://github.com/VAISHALI311/devops-shop-app.git'
            }
        }

        stage('Login to AWS ECR') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'aws-credentials', usernameVariable: 'AWS_ACCESS_KEY_ID', passwordVariable: 'AWS_SECRET_ACCESS_KEY')]) {
                    sh '''
                    aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
                    aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $FRONTEND_REPO

                    aws ecr get-login-password --region $AWS_REGION | \
                    docker login --username AWS --password-stdin $BACKEND_REPO
                    '''
                }
            }
        }

        stage('Build Frontend Docker Image') {
            steps {
                sh '''
                cd frontend
                docker build -t frontend-image .
                docker tag frontend-image:latest $FRONTEND_REPO:latest
                '''
            }
        }

        stage('Build Backend Docker Image') {
            steps {
                sh '''
                cd backend
                docker build -t backend-image .
                docker tag backend-image:latest $BACKEND_REPO:latest
                '''
            }
        }

        stage('Push Images to ECR') {
            steps {
                sh '''
                docker push $FRONTEND_REPO:latest
                docker push $BACKEND_REPO:latest
                '''
            }
        }
    }
}
