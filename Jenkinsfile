pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "ghcr.io/prompipat/myapi"
        DOCKER_TAG   = "${BUILD_NUMBER}"
        K8S_NAMESPACE = "dev"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
                echo "Checked out code from SCM"
            }
        }

        stage ('Install Dependencies') {
            steps {
                sh '''
                    pip3 install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Unit Tests - mul10') {
            steps {
                sh '''
                    pip3 install pytest httpx --break-system-packages
                    python3 -m pytest tests/test_mul10.py -v \
                        --junitxml=test-results/unit-test.xml
                '''
            }
            post {
                always {
                    junit 'test-results/unit-test.xml'
                }
            }
        }

        stage('Robot Framework Test - mul10') {
            steps {
                sh '''
                    robot --variable BASE_URL:http://192.168.49.2:30080 \
                          --outputdir robot-results \
                          ../test_robot_SDPX/tests/test_mul10.robot
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'robot-results/*', allowEmptyArchive: true
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .
                    docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest
                '''
                echo "Build Docker Image successfully: ${DOCKER_IMAGE}:${DOCKER_TAG}"
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'ghcr-credentials',
                    usernameVariable: 'GITHUB_USER',
                    passwordVariable: 'GITHUB_TOKEN'
                )]) {
                    sh '''
                        echo $GITHUB_TOKEN | docker login ghcr.io \
                             -u $GITHUB_USER --password-stdin
                        docker push ${DOCKER_IMAGE}:${DOCKER_TAG}
                        docker push ${DOCKER_IMAGE}:latest
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl set image deployment/api-deployment \
                        myapi=${DOCKER_IMAGE}:${DOCKER_TAG} \
                        -n ${K8S_NAMESPACE}
                    kubectl rollout status deployment/api-deployment \
                        -n ${K8S_NAMESPACE}
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Please check the logs for details."
        }
    }
}