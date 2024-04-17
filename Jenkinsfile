
pipeline {
    agent any
   
    
    stages {
        stage('checkout') {
            steps {
               checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'python207', url: 'https://github.com/demesne2001/JewelWebReportBack.git']])
                echo 'checkout done'
            }
        }
        

        stage('Docker Image') {
            steps {
                
                script{
                    def a=0
                    bat 'docker build . -f dockerfile.txt -t  webjewelreportback'
                    a=1
                    if(a>0)
                    {
                         bat 'docker stop  webjewelreportback'
                         bat 'docker rm  webjewelreportback'
                    }
                }
                echo 'Docker Image done'
            }
        }
        stage('Docker Run') {
            steps {
                script{
                    bat 'docker run -p 52202:52202 -it -v SharedImages:/BackendJewelWebReport/Utility/Image -v SharePDF:/BackendJewelWebReport/Utility/PDF -v ShareLogFile:/BackendJewelWebReport/Utility/Logfile -d --name  webjewelreportback  webjewelreportback'
                }
                echo 'Docker Running'
            }
        }
        stage('Docker push') {
            steps {
                // script{
                //     bat 'docker login -u patelom0910 -p 09102001Om'
                // }
                echo 'Docker push done'
            }
        }
    }
}