pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Docker image build ediliyor...'
                sh 'docker build -t flask-weather .'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Var olan container durduruluyor (varsa)...'
                sh 'docker stop weatherApp || true'
                sh 'docker rm weatherApp || true'

                echo 'Yeni container başlatılıyor...'
                sh 'docker run -d -p 5000:5000 --name weatherApp flask-weather'
            }
        }
    }
}

