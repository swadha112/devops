/* pipeline {
    agent any  

    tools {
        maven 'Maven 3.9.11'  
        jdk 'Java 21.0.8'        
    }

    stages {
        stage('Build') {
            steps {
                script {
                    // Maven build command
                    echo 'Building the Maven project...'
                    sh 'mvn clean install'  // This will clean and build your Maven project
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    // Maven test command
                    echo 'Running tests...'
                    sh 'mvn test'  // This will run your unit tests using Maven
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    echo 'Deploying the application...'
                    echo 'Deploy command needs to be customized based on your deployment method.'
                }
            }
        }
    }

    post {
        always {
            echo 'This runs after the pipeline, no matter the result.'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
 */
/* 
node {
    // Define tools
    def mvnHome = tool 'Maven 3.9.11'
    def javaHome = tool 'Java 21.0.8'
    
    // Set environment
    env.JAVA_HOME = javaHome
    env.PATH = "${javaHome}/bin:${env.PATH}"
    
    try {
        // Stage 1: Checkout
        stage('Checkout') {
            echo 'Checking out source code...'
            checkout scm
        }
        
        // Stage 2: Build
        stage('Build') {
            echo 'Building the application...'
            sh "${mvnHome}/bin/mvn clean compile"
        }
        
        // Stage 3: Test
        stage('Test') {
            echo 'Running tests...'
            sh "${mvnHome}/bin/mvn test"
            
        }
        
        // Stage 4: Deploy
        stage('Deploy') {
            echo 'Deploying application...'
        }
        
    } catch (Exception e) {
        // Mark build as failed
        currentBuild.result = 'FAILURE'
        echo "Build failed: ${e.getMessage()}"
        throw e
        
    } finally {
        // Clean up workspace
        echo 'Cleaning up...'
        cleanWs()
    }
}
 */

 pipeline {
    agent any
    
    environment {
        PYTHON_HOME = '/usr/bin/python3'
        PATH = "${PYTHON_HOME}/bin:${env.PATH}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout code from repository
                checkout scm
            }
        }

        stage('Setup Environment') {
            steps {
                // Set up environment and install dependencies
                sh 'python3 -m venv venv'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run pytest with the necessary options
                sh './venv/bin/pytest --maxfail=1 --disable-warnings -q'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
        success {
            echo 'Tests passed.'
        }
        failure {
            echo 'Tests failed.'
        }
    }
}
