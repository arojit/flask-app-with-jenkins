node {
    stage('SCM Checkout'){
        git branch: 'main', url: 'https://github.com/arojit/flask-app-with-jenkins.git'
    }

    stage('Docker Build'){
        sh 'docker build -t arojit007/flask-web-app:1.0.0 .'
    }

    stage('Push Docker Image'){
        withCredentials([string(credentialsId: 'dokcer-password', variable: 'Docker_Hub_Password')]) {
            sh "docker login -u arojit007 -p ${Docker_Hub_Password}"
        }
        sh 'docker push arojit007/flask-web-app:1.0.0'
    }

    stage('Run Container on Dev Server'){
        def dockerRun = 'docker rm -f flask-web-app 2> /dev/null || true && docker run -p 5000:5000 -d --name flask-web-app arojit007/flask-web-app:1.0.0'
        sshagent(['dev-server']) {
            sh "ssh -o StrictHostKeyChecking=no ec2-user@18.204.243.142 '${dockerRun}'"
        }
    }
}