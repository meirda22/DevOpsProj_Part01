pipeline {
    agent any
        stages{
            stage('checkout'){
                steps{
                    script{
                        properties([pipelineTriggers([pollSCM('H/30 * * * *')])])
                    }
                    git'https://github.com/meirda22/DevOpsProj_Part01.git'
                }
            }
            stage('run rest_app'){
                steps{
                    script{
                        returnValue = bat 'start /min python rest_app.py'
                            if (returnValue == 0) {
                                echo 'Batch file executed successfully'
                            } else {
                                echo 'Batch file execution failed'
                        }
                    }
                }   
            }
            stage('run web_app'){
                steps{
                    bat 'start /min python web_app.py'
                }
            }
            stage('run backend_testing'){
                steps{
                    bat 'start python backend_testing.py'
                }
            }
            stage('run frontend_testing'){
                steps{
                    bat 'start python frontend_testing.py'
                }
            }
            stage('run combined_testing'){
                steps{
                    bat 'start python combind_testing.py'
                }
            }
            stage('run clean_environment'){
                steps{
                    bat 'start python clean_environment.py'
                }
            }
        }
}
