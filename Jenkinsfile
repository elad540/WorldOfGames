pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'your_credentials_id', url: 'https://github.com/elad540/WorldOfGames.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t WOG .'
            }
        }
        stage('Run') {
            steps {
                sh 'docker run -p 8777:8777 -v C:/Users/elad5/PycharmProjects/29/WorldOfGames/sources/Scores.txt:/app/Scores.txt WOG'
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
                sh 'docker stop WOG'
                sh 'docker push WOG'
            }
        }
    }
}
// In this Jenkinsfile, the pipeline first checks out the repository, then it builds a Docker image, runs the container with the specified port and mounted file, runs the e2e.py file to test the scores web service, and finally, if the tests pass, it stops the container and pushes the image to DockerHub.
// It's worth noting that you need to make sure you have the correct credentials to access your repo, and also that you need to replace the placeholders with the correct values such as your repo url, image name, and container name.