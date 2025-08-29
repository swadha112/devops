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
    // Define environment variables for Maven and Java
    def MAVEN_HOME = '/opt/homebrew/opt/maven'
    def JAVA_HOME = '/opt/homebrew/opt/openjdk'
    def PATH = "${JAVA_HOME}/bin:${MAVEN_HOME}/bin:${env.PATH}"

    try {
        stage('Checkout') {
            // Checkout code from repository
            checkout scm
        }

        stage('Build') {
            // Run the Maven build command
            echo 'Building the project...'
            sh 'mvn clean install'
        }

        stage('Test') {
            // Run the Maven test command
            echo 'Running tests...'
            sh 'mvn test'
        }

        stage('Deploy') {
            // Deploy the application
            echo 'Deploying the application...'
            
        }

    } catch (Exception e) {
        // Catch errors and mark the build as failed
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        // Cleanup or notifications if necessary
        echo 'Pipeline execution completed.'
    }
}
