// Define outside of pipeline block
def CI_CREDS = env.BRANCH_NAME.replaceAll('\\/','-');
echo CI_CREDS
pipeline {
agent any
	environment {
        SF_CREDS = credentials("${CI_CREDS}-sf-creds")
        BRRANCH_NAME = "${env.BRANCH_NAME}"
    }  
stages {
			stage('Package CI Sandbox') {
				steps{
					echo "CI_CREDS name:: ${CI_CREDS}"
				}
			}
		}
}
