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
 

 node {
  stage('Checkout') {
    checkout scm
  }

  stage('Set up Python venv & deps') {
    sh '''
      python3 -m venv venv
      ./venv/bin/pip install --upgrade pip
      ./venv/bin/pip install -r requirements.txt
      mkdir -p reports
    '''
  }

  stage('Run tests (headless)') {
    withEnv(['HEADLESS=1']) {
      sh '''
        ./venv/bin/pytest --junitxml=reports/junit.xml
      '''
    }
  }

  stage('Publish results') {
    junit 'reports/junit.xml'
    archiveArtifacts artifacts: 'reports/**/*.xml', fingerprint: true, onlyIfSuccessful: false
  }
}
