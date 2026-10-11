pipeline {
    agent any

    environment {
        PROJECT_NAME = "devops-demo"
        // Try to find Python executable
        PYTHON_PATH = "python"
        PYTHON3_PATH = "python3"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '==> Source code checked out from GitHub'
                echo "==> Repository: ${env.GIT_URL}"
                echo "==> Branch: ${env.GIT_BRANCH}"
            }
        }

        stage('Prepare') {
            steps {
                echo '==> Checking for Python installation...'
                script {
                    // Try to find Python executable
                    def pythonExe = bat(script: 'where python 2>nul', returnStdout: true).trim()
                    def python3Exe = bat(script: 'where python3 2>nul', returnStdout: true).trim()

                    if (pythonExe) {
                        echo "Found Python at: ${pythonExe}"
                        env.PYTHON_EXE = "python"
                    } else if (python3Exe) {
                        echo "Found Python3 at: ${python3Exe}"
                        env.PYTHON_EXE = "python3"
                    } else {
                        // Check if Python is in a standard location
                        bat '''
                            @echo off
                            echo Looking for Python in common locations...
                            where python
                            where python3
                            echo.
                            echo If no Python found, please ensure Python is installed and in PATH
                        '''
                        error("Python not found! Please install Python 3.x and add it to PATH.")
                    }
                }
            }
        }

        stage('Build') {
            steps {
                echo '==> Build stage: checking Python and syntax...'
                script {
                    def pythonCmd = env.PYTHON_EXE ?: "python"
                    bat """
                        @echo off
                        echo Using: ${pythonCmd}
                        ${pythonCmd} --version
                        echo.
                        echo Checking syntax of all Python files:
                        for %%f in (*.py) do (
                            echo Checking %%f...
                            ${pythonCmd} -m py_compile "%%f"
                            if errorlevel 1 (
                                echo ERROR: Syntax error in %%f
                                exit /b 1
                            )
                        )
                        echo Syntax check passed for all Python files.
                    """
                }
            }
        }

        stage('Test') {
            steps {
                echo '==> Test stage: running unit tests...'
                script {
                    def pythonCmd = env.PYTHON_EXE ?: "python"
                    bat """
                        @echo off
                        echo Using: ${pythonCmd}
                        echo Installing dependencies...
                        ${pythonCmd} -m pip install --quiet flask pytest
                        echo.
                        echo Running tests:
                        ${pythonCmd} -m pytest test_app.py -v
                        if errorlevel 1 (
                            echo.
                            echo !!! UNIT TESTS FAILED !!!
                            exit /b 1
                        )
                    """
                }
            }
        }

        stage('Result') {
            steps {
                script {
                    if (currentBuild.result == null || currentBuild.result == 'SUCCESS') {
                        echo '=================================================='
                        echo '  BUILD SUCCESS - Pipeline completed successfully'
                        echo '  Stages: Checkout, Prepare, Build, Test'
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