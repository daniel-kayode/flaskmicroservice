pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-change-app:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your Git repository
                git 'https://github.com/daniel-kayode/flaskmicroservice.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE}", "-f app/Dockerfile .")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container
                    docker.image("${DOCKER_IMAGE}").run('-p 8080:8080')
                }
            }

            post {
                always {
                    // Clean up: stop and remove Docker container
                    script {
                        docker.container("${DOCKER_IMAGE}").stop()
                        docker.container("${DOCKER_IMAGE}").remove(force: true)
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                // Stop the existing container if running
                    sh 'docker stop flask-change-app || true'
                    // Remove the existing container if exists
                    sh 'docker rm flask-change-app || true'
                    // Run the new container with port mapping
                    sh 'docker run -d -p 8080:8080 --name flask-change-app ${DOCKER_IMAGE}'
            }
        }
    }

    // Define post-build actions if necessary
    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed :('
        }
    }
}
