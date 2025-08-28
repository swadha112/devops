node {
    // Define Maven and JDK tool installations as configured in Jenkins
    def mvnHome = tool name: 'Maven 3.9.11', type: 'Maven'
    def jdkHome = tool name: 'Java 21.0.8', type: 'JDK'

    // Set environment variables for Maven and JDK
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
            sh 'mvn clean install'
        }

        stage('Test') {
            echo 'Running tests...'
            sh 'mvn test'
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
