pipeline {
    agent {
        label 'windows'
    }
    
    stages {


        stage('Build') {
            steps {
                sh 'docker build -t fashion_mnist .'
            }
        }
        

	stage('Run') {
            steps {
                sh 'docker run -p 5000:5000 --name=fmn fashion_mnist'
            }
        }

        
        
    }
}
