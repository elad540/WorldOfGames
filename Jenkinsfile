pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'your_credentials_id', url: 'https://github.com/your_repository.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t your_image_name .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -p 8777:8777 -v /path/to/Scores.txt:/app/Scores.txt your_image_name'
            }
        }
        stage('Test') {
            steps {
                sh 'python e2e.py'
                sh 'if [ $? -ne 0 ]; then exit 1; fi'
            }
        }
        stage('Finalize') {
            steps {
                sh 'docker stop your_container_name'
                sh 'docker push your_image_name'
            }
        }
    }
}
