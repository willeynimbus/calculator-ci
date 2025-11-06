pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        AWS_REGION = 'ap-south-1'
        APP_NAME = 'calculator-ci'
        AWS_CREDENTIALS = credentials('aws-creds')
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

        stage('Setup SAM CLI'){
            steps{
                sh '''
                    aws configure set aws_access_key_id $AWS_CREDENTIALS_USR
                    aws configure set aws_secret_access_key $AWS_CREDENTIALS_PSW
                    aws configure set region $AWS_REGION
                '''
            }
        }

        stage('Deploy to the AWS'){
            steps{
                withAWS(credentials: 'aws-creds', region: 'ap-south-1'){
                    sh '''
                        sam build
                        sam deploy --stack-name calculator-stack \
                                   --template-file template.yaml \
                                   --capabilities CAPABILITY_IAM \
                                   --region $AWS_REGION \
                                   --no-confirm-changeset \
                                   --resolve-s3
                    '''
                }
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
