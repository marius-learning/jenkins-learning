pipeline {
    agent any

    environment {
        DOCKERHUB_REPO='flask-app'
        GITHUB_REPO='jenkins-learning'
        DOCKERHUB_CREDS = credentials('DOCKERHUB')
    }

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main', url: "https://github.com/marius-learning/${GITHUB_REPO}"
                sh 'ls *'
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_CREDS_USR/$DOCKERHUB_REPO:$BUILD_NUMBER .'
            }
        }

        stage('DockerHub Login') {
            steps {
                sh 'echo $DOCKERHUB_CREDS_PSW | docker login -u $DOCKERHUB_CREDS_USR --password-stdin'
            }
        }

        stage('Push image into DockerHub Repo') {
            steps {
                sh 'docker push $DOCKERHUB_CREDS_USR/$DOCKERHUB_REPO:$BUILD_NUMBER'
            }
        }

        stage('Trigger downstream_job') {
            steps {
                build job: 'downstream_job', parameters: [string(name: 'IMAGE_TAG', value: env.BUILD_NUMBER)]
            }
        }
    }
    post {
        always {
            sh 'docker logout'
            sh 'docker rmi $(docker images --filter "label=app=flask" -q)'
        }
    }
}
