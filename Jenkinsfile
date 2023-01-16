pipeline {
    agent any
    stages {
        stage('checkout') {
            steps {
                script {
                    properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                }
                git 'https://github.com/meirda22/DevOpsProj_Part01.git'
            }
        }
        stage('run rest_app') {
            steps {
                script {
                    if (checkOs() == 'Windows'){
                        bat 'start /min python rest_app.py'
                    }else {
                        sh 'nohup python rest_app.py &'
                    }
                }
            }
        }
    }
}
