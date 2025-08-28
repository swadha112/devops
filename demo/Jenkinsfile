node {
    stage('Checkout') {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[url: 'https://github.com/keyurpatil06/jenkins-test.git']]
        ])
    }

    stage('Build') {
        withEnv(["JAVA_HOME=${tool 'JDK17'}", "PATH+JAVA=${tool 'JDK17'}/bin", "PATH+MAVEN=${tool 'maven'}/bin"]) {
            sh 'mvn clean package'
        }
    }

    stage('Test') {
        withEnv(["JAVA_HOME=${tool 'JDK17'}", "PATH+JAVA=${tool 'JDK17'}/bin", "PATH+MAVEN=${tool 'maven'}/bin"]) {
            sh 'mvn test'
        }
    }

    stage('Archive') {
        archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
    }
}