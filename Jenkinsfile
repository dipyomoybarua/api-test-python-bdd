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
                    bat '''
                        python -m venv venv
                        call venv\\Scripts\\activate
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

                    bat """
                        call venv\\Scripts\\activate
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