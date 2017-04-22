pipeline {
  agent any
  stages {
    stage('VM creation') {
      steps {
        sh '''echo 'triggering vm creation script'
python vm_creation.py
'''
      }
    }
  }
}