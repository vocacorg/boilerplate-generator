pipeline{
    agent any
    stages{
        stage("Clone"){
            steps{
                cleanWs()
                script {
                    // Get the input
                    def userInput = input(
                        id: 'userInput', message: 'Please enter project information',
                        parameters: [
                            string(defaultValue: 'terraform-provider-template',
                                    description: 'Enter the repository name:',
                                    name: 'RepositoryName'),
                            string(defaultValue: 'Sample Description',
                                    description: 'Enter repository description',
                                    name: 'RepositoryDesc'),
                        ])
                    
                    env.REPOSTORY_NAME = userInput.RepositoryName?:''
                    env.REPOSTORY_DESC = userInput.RepositoryDesc?:''
                }

                echo "========== Target Repository: $REPOSTORY_NAME, Description: $REPOSTORY_DESC ========="

                echo "========== Cloning the git repository: " + env.BRANCH_NAME
                git branch: 'master', url: 'https://github.com/vocacorg/boilerplate-generator.git'
                echo "Content in working directory"
                sh "ls -la ."
            }
            post{
                success{
                    echo "======== Repository cloned successfully ========"
                }
                failure{
                    echo "======== Unable to clone the repository ========"
                }
            }
        }
        stage("Build"){
            steps{
                echo "========== Building the repository ==========="
                sh 'chmod 744 generator.sh'
                sh "./generator.sh $REPOSTORY_NAME $REPOSTORY_DESC"
            }
            post{
                success{
                    echo "======== Build completed successfully ========"
                }
                failure{
                    echo "======== Unable to build the code ========"
                }
            }
        }
    }
    post{
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}