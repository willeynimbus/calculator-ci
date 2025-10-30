pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1'
        APP_NAME = 'calculator-ci'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                sh '''
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo '🧪 Running unit tests...'
                sh '''
                pytest --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning workspace...'
            cleanWs()
        }
        success {
            echo '✅ Tests completed successfully!'
        }
        failure {
            echo '❌ Tests failed. Check logs for details.'
        }
    }
}
