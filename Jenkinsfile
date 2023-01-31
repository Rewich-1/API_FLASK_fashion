pipeline {
    agent any
    
    stages {


        stage('Build') {
            steps {
                bat  'docker build -t fashion_mnist .'
            }
        }
        

	stage('Run') {
            steps {
                bat  'docker run -p 5000:5000 --name=fmn fashion_mnist'
            }
        }

        
        
    }
}
