pipeline {
    agent any
    
    stages {

	stage("Testing the model"){
      		steps{
       		echo 'testing'
        	
      		}
    	}

        stage('Build') {
            	steps {
                bat 'docker build -t fashion_mnist .'
            	}
        }
        

	stage('Run') {
            	steps {
               	bat 'docker run -d -p 5000:5000 --name=fmn fashion_mnist'
            	}
        }
	
	stage("Testing the RESTAPI"){
      		steps{
        	echo 'testing the RESTAPI'
        	
      		}
	}

        
        
    }
}
