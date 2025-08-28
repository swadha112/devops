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


 node {
    // Tools configuration - you can set these in the global Jenkins configuration if needed
    def mvnHome = tool 'Maven 3.9.11'
    def jdkHome = tool 'Java 21.0.8'

    // Set environment variables for Maven and JDK
    environment {
        PATH = "${mvnHome}/bin:${jdkHome}/bin:${env.PATH}"
    }

    try {
        stage('Build') {
            echo 'Building the Maven project...'
            // Maven build command
            sh 'mvn clean install'  // This will clean and build your Maven project
        }

        stage('Test') {
            echo 'Running tests...'
            // Maven test command
            sh 'mvn test'  // This will run your unit tests using Maven
        }

        stage('Deploy') {
            echo 'Deploying the application...'
            // Custom deploy commands
            echo 'Deploy command needs to be customized based on your deployment method.'
        }

    } catch (Exception e) {
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        // This will always be executed
        echo 'This runs after the pipeline, no matter the result.'
    }
}
