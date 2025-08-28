pipeline {
    agent any  /

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
