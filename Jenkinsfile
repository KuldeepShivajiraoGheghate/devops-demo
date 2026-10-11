pipeline {
    agent any

    environment {
        PROJECT_NAME = "devops-demo"
        // Common Python installation paths on Windows
        PYTHON_PATH = "C:\\Users\\asus\\anaconda3\\python.exe"
        PYTHON3_PATH = "C:\\Users\\asus\\anaconda3\\python.exe"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '==> Source code checked out from GitHub'
                echo "==> Repository: ${env.GIT_URL}"
                echo "==> Branch: ${env.GIT_BRANCH}"
            }
        }

        stage('Build') {
            steps {
                echo '==> Build stage: checking Python and syntax...'
                bat '''
                    @echo off
                    echo Python path: %PYTHON_PATH%
                    "%PYTHON_PATH%" --version
                    echo.
                    echo Checking syntax of all Python files:
                    for %%f in (*.py) do (
                        echo Checking %%f...
                        "%PYTHON_PATH%" -m py_compile "%%f"
                        if errorlevel 1 (
                            echo ERROR: Syntax error in %%f
                            exit /b 1
                        )
                    )
                    echo Syntax check passed for all Python files.
                '''
            }
        }

        stage('Test') {
            steps {
                echo '==> Test stage: running unit tests...'
                bat '''
                    @echo off
                    echo Python path: %PYTHON_PATH%
                    echo Installing dependencies...
                    "%PYTHON_PATH%" -m pip install --quiet flask pytest
                    echo.
                    echo Running tests:
                    "%PYTHON_PATH%" -m pytest test_app.py -v
                    if errorlevel 1 (
                        echo.
                        echo !!! UNIT TESTS FAILED !!!
                        exit /b 1
                    )
                '''
            }
        }

        stage('Result') {
            steps {
                script {
                    if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                        echo '=================================================='
                        echo '  BUILD SUCCESS - Pipeline completed successfully'
                        echo '  Stages: Checkout, Build, Test'
                        echo '=================================================='
                    } else {
                        echo '=================================================='
                        echo '  BUILD FAILED - Check console output for details'
                        echo '=================================================='
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline finished: SUCCESS'
        }
        failure {
            echo 'Pipeline finished: FAILURE'
        }
        always {
            echo 'Pipeline finished. See console output for details.'
        }
    }
}