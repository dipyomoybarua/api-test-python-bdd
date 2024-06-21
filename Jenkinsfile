pipeline {
    agent any

    environment {
        GITHUB_CREDENTIALS = 'github-credentials-id'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: env.GITHUB_CREDENTIALS, url: 'https://github.com/dipyomoybarua/api-test-python-behave.git'
            }
        }
        stage('Set up Python Environment') {
            steps {
                script {
                    // Install dependencies using a Python virtual environment
                    sh '''
                        python -m venv venv
                        . venv/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        stage('Run Tests in Parallel') {
            steps {
                script {
                    def parallelism = 3

                    sh """
                        . venv/bin/activate
                        pytest -n ${parallelism}
                    """
                }
            }
        }
    }

    post {
        success {
            archiveArtifacts artifacts: '**/results/*', allowEmptyArchive: true
            echo 'Pipeline completed successfully.'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
