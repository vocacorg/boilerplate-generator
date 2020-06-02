pipeline{
    agent any
    stages{
        stage("Clone"){
            steps{
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
                sh "./generator.sh terraform-provider-bitbucket 'bitbucket provider repository'"
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