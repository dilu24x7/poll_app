pipeline {
  agent any
  stages {
    stage('Code Checkout') {
      steps {
        git(changelog: true, url: 'https://github.com/dilu24x7/poll_app', branch: 'master', credentialsId: '12', poll: true)
      }
    }
  }
}