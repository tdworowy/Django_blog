pipeline {

    agent { label 'Slave_ubuntu'}

    stages {
        stage("Clean workspcae"){
            steps{
                cleanWs()
            }
        }
        stage("Pull changes from git"){
           steps{
                git 'http://github.com/tdworowy/Django_blog.git'
            }
        }
        stage("Static code analize"){
           steps{
                script{
                    sh 'sudo pylint --output-format=json Example > pylint_report.json || true'
                }

            }

        }
        stage('Build image') {
            steps {
               script{
               docker.build("blog")
               }
            }
        }
         stage('Run Blog') {
            steps {
               script{
                sh 'docker run -d --name blog -p 8083:8083 blog:latest'
               }
            }
        }
    stage('Run Tests')
    {
        agent { label 'master'}
        steps{
            build 'blogTests'
        }
    }
    stage('Blog logs'){
        steps{
            script{
                sh 'docker logs blog 2>&1 | tee logs.txt'
            }

        }
    }
    }
     post {
        always {
             script{
                sh 'sudo chmod 777 clear_docker.sh'
                sh './clear_docker.sh'
                archive 'pylint_report.json'
                archive 'logs.txt'

            }
    }
    }


}