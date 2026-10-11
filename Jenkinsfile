/**
 * Jenkinsfile - Declarative Pipeline for the devops-demo project.
 *
 * This pipeline runs on every build and performs the following stages:
 *   1. Checkout - Retrieve the source code from the GitHub repository.
 *   2. Build    - Check the Python version and perform a syntax check.
 *   3. Test     - Run the unit tests. The pipeline fails if any test fails.
 *   4. Result   - Display a clear success or failure message.
 *
 * The pipeline is configured as "Pipeline script from SCM" so Jenkins
 * reads this file directly from the repository (Jenkinsfile path).
 */

pipeline {
    agent any

    environment {
        // Define environment variables used across stages.
        PROJECT_NAME = "devops-demo"
        PYTHON_VERSION = "3"
    }

    stages {

        stage('Checkout') {
            steps {
                // SCM checkout is handled by the "Pipeline script from SCM"
                // configuration in the job. This stage confirms the checkout.
                echo "==> Checking out source code from GitHub..."
                echo "==> Repository: ${env.GIT_URL}"
                echo "==> Branch: ${env.GIT_BRANCH}"
            }
        }

        stage('Build') {
            steps {
                echo "==> Build stage: checking Python and syntax..."
                sh '''
                    echo "Python version:"
                    python3 --version
                    echo ""
                    echo "Checking Python syntax of all .py files:"
                    find . -name "*.py" -print0 | xargs -0 -I {} python3 -m py_compile {}
                    echo "Syntax check passed."
                '''
            }
        }

        stage('Test') {
            steps {
                echo "==> Test stage: running unit tests..."
                sh '''
                    echo "Installing test dependencies (if any)..."
                    python3 -m pip install --quiet --upgrade pip
                    python3 -m pip install --quiet flask pytest
                    echo ""
                    echo "Running unit tests:"
                    python3 -m pytest test_app.py -v
                '''
            }
        }

        stage('Result') {
            steps {
                script {
                    if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                        echo "=================================================="
                        echo "  BUILD SUCCESS - ${env.PROJECT_NAME} pipeline passed."
                        echo "  All stages completed: Checkout, Build, Test."
                        echo "=================================================="
                    } else {
                        echo "=================================================="
                        echo "  BUILD FAILED - ${env.PROJECT_NAME} pipeline failed."
                        echo "  Check the console output above for details."
                        echo "=================================================="
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Pipeline finished: SUCCESS"
        }
        failure {
            echo "Pipeline finished: FAILURE"
        }
        always {
            echo "Pipeline finished. See console output for details."
        }
    }
}