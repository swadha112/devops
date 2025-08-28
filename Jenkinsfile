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
    // Use Maven and JDK tools configured in Jenkins
    def mvnHome = tool name: 'Maven 3.9.11', type: 'Maven'
    def jdkHome = tool name: 'Java 21.0.8', type: 'JDK'

    environment {
        MAVEN_HOME = mvnHome
        JAVA_HOME = jdkHome
        PATH = "${MAVEN_HOME}/bin:${JAVA_HOME}/bin:${env.PATH}"
    }

    try {
        stage('Checkout') {
            echo 'Checking out the repository...'
            checkout scm
        }

        stage('Build') {
            echo 'Building the Maven project...'
            sh 'mvn clean install'  // Using 'mvn' without the explicit path
        }

        stage('Test') {
            echo 'Running tests...'
            sh 'mvn test'  // Running tests using Maven
        }

        stage('Deploy') {
            echo 'Deploying the application...'
            echo 'Deploy command needs to be customized based on your deployment method.'
        }

    } catch (Exception e) {
        currentBuild.result = 'FAILURE'
        throw e
    } finally {
        echo 'Pipeline execution completed.'
    }
}
