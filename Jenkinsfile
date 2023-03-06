// Define outside of pipeline block
def CI_CREDS = env.BRANCH_NAME.replaceAll('\\/','-');
echo CI_CREDS
pipeline {
agent any
stages {
			stage('Package CI Sandbox') {
				steps{
					echo "CI_CREDS name:: ${CI_CREDS}"
				}
			}
		}
}
