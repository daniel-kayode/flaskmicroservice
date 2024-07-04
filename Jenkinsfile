pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-change-app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git  branch: 'main', url:'https://github.com/daniel-kayode/flaskmicroservice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_IMAGE}", "-f Dockerfile .")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    sh "docker run -d --name ${DOCKER_IMAGE}_cont -p 8080:8080 ${DOCKER_IMAGE} "
                }
            }
            post {
                always {
                    script {
                        sleep 30
                        sh "docker stop ${DOCKER_IMAGE}"
                        sh "docker rm ${DOCKER_IMAGE}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed :('
        }
    }
}
