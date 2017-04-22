pipeline {
  agent any
  stages {
    stage('VM create call') {
      steps {
        sh '''python vm_create.py
'''
      }
    }
    stage('VM status call') {
      steps {
        waitUntil() {
          timeout(unit: 'HOURS', time: 3) {
            retry(count: 4) {
              sh 'python vm_status.py'
              sleep(time: 1, unit: 'HOURS')
            }
            
          }
          
        }
        
      }
    }
    stage('Build') {
      steps {
        sh 'echo \'build steps\''
      }
    }
    stage('Deploy') {
      steps {
        sh 'python deploy.py'
      }
    }
  }
}