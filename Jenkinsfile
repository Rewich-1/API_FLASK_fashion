pipeline {
    agent any
    
    stages {


        stage('Build') {
            steps {
                sh 'docker build -t fashion_mnist .'
            }
        }
        

	stage('Run') {
            steps {
               sh 'docker run -d -p 5000:5000 --name=fmn fashion_mnist'
            }
        }

        
        
    }
}
