node {
    stage('Checkout') {
        checkout([$class: 'GitSCM',
                  branches: [[name: '*/main']],
                  userRemoteConfigs: [[url: 'https://github.com/swadha112/devops.git']]
        ])
    }

    stage('Build') {
        withEnv(["JAVA_HOME=${tool 'JDK21'}", "PATH+JAVA=${tool 'JDK21'}/bin", "PATH+MAVEN=${tool 'maven'}/bin"]) {
            sh 'mvn clean package'
        }
    }

    stage('Test') {
        withEnv(["JAVA_HOME=${tool 'JDK21'}", "PATH+JAVA=${tool 'JDK21'}/bin", "PATH+MAVEN=${tool 'maven'}/bin"]) {
            sh 'mvn test'
        }
    }

    stage('Archive') {
        archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
    }
}