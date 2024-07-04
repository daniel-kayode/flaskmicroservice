pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-change-app'
        DOCKERHUB_REPO = 'kcaher/flaskmicroservice'
//        DOCKERHUB_CREDENTIALS_ID = 
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
                        sh "docker stop ${DOCKER_IMAGE}_cont"
                        sh "docker rm ${DOCKER_IMAGE}_cont"
                    }
                }
            }
            
        }

        stage('Push DOCKER_IMAGE to dockerhub') {
            steps {
                script {
                    //Push to my dockerhub 
                    //sh "docker login"
                    sh "docker tag ${DOCKER_IMAGE} DOCKERHUB_REPO}"
                    sh "docker push kcaher/${DOCKER_IMAGE}"
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
