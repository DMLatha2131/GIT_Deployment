// Define outside of pipeline block
def CI_CREDS = env.BRANCH_NAME;
echo CI_CREDS
pipeline {
agent any
	environment {
        SF_CREDS = credentials("${CI_CREDS}-sf-creds")
        BRRANCH_NAME = "${env.BRANCH_NAME}"
    }  
stages {
			stages {
        stage('Package CI Sandbox') {
            steps {
                script {
                    withCredentials ([usernamePassword(credentialsId: 'github-cicd', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASSWORD')])
                    {
                       sh '''
                            git config diff.renamelimit 999999
                            git fetch --tags https://${GIT_USER}:${GIT_PASSWORD}@github.dxc.com/DXC-SFDC/DXC-enterpriseservices.git ${BRRANCH_NAME}
                            git tag
                            
                            printenv
                            
                            git diff --name-only ${BUILD_START_TAG} HEAD > delta.txt
                            
                            cat delta.txt
                            
                            sed '/^Jenkins/d' delta.txt
                            
                            cat delta.txt
                            
                            sed -i "s/\\\\$/\\\\\\\\\\\\\\\\$/g" delta.txt
                            
                            cat delta.txt
                            sed -i "s/\\\\ /\\\\\\\\\\\\\\\\ /g" delta.txt
                            
                            cat delta.txt
                            sed -i "s/$/\\*/" delta.txt
                            
                            cat delta.txt
                            
                            sed -i "s/\\(.*\\/aura\\/.*\\/\\).*/\\1\\*/" delta.txt
                            
                            cat delta.txt
                            
                            mkdir deployment
                            cat delta.txt | xargs -I % sh -c "cp --parents % deployment"
                            
                            ls -R deployment
                            cd ${CI_FOLDER_PATH}
                            npm install
                            npm run package
                            ls -R ../../deployment
                        '''
                    }
                }
            }
        }
    
}
