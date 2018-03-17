pipeline {
     //environment {

     //}
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
                //sh 'docker run -d --name blog -p 127.0.0.1:8082:8082 blog:latest python Django_blog/Example/Example1/blog/Utils/startServer.py 8082'
               sh 'docker run -d --name blog -p 127.0.0.1:8082:8082 blog:latest'

               }
            }
        }
    }
}

