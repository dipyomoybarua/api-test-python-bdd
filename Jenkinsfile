pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-credentials-id'
        PYTHONPATH = "${env.WORKSPACE}"
    }

    options {
        timestamps() 
        buildDiscarder(logRotator(numToKeepStr: '10')) 
    }

    triggers {
        githubPush() // Trigger the pipeline on push events from GitHub
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: env.GITHUB_CREDENTIALS, url: 'https://github.com/dipyomoybarua/api-test-python-behave.git'
            }
        }

        stage('Build') {
            steps {
                script {
                    // Example: Build your code
                    bat 'echo Building your code...'
                    // Add your build commands here
                }
            }
        }

        stage('Automated Tests') {
            steps {
                script {
                    // Example: Run automated tests
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                        pytest
                    '''
                }
            }
        }

        stage('Manual Approval') {
            steps {
                input message: 'Proceed with deployment?', ok: 'Deploy'
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '**/reports/*', allowEmptyArchive: true
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
