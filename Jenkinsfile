pipeline {
  agent any

  environment {
    DOCKER_IMAGE = 'flask-change-app'
    DOCKER_REPO = 'kcaher/flaskmicroservice'
    DOCKER_CREDENTIALS_ID = '7c665306-9cf4-4180-8a57-ae82e5466a45' // Update with your Docker Hub credentials ID in Jenkins
  }

  stages {
    stage('Checkout') {
      steps {
        git branch: 'main', url:'https://github.com/daniel-kayode/flaskmicroservice.git'
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
        withCredentials([usernamePassword(credentialsId: "${DOCKER_CREDENTIALS_ID}", usernameVariable: 'kcaher', passwordVariable: 'DOCKER_PASS')]) {
          sh "docker login -u ${kcaher} -p ${DOCKER_PASS}"
          sh "docker tag ${DOCKER_IMAGE} ${DOCKER_REPO}"
          sh "docker push ${DOCKER_REPO}"
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
