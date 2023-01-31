pipeline {
    agent any
    
    stages {


        stage('Build') {
            steps {
                bat  'docker build -t my-flask-app:latest .'
            }
        }
        

	stage('Run') {
            steps {
                bat  'docker run -p 5000:5000 -d my-flask-app:latest'
            }
        }

        
        
    }
}
