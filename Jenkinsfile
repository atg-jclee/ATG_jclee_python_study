pipeline {
    environment {
        // registry = "https://registry.atg.re.kr"
        registry = "218.155.189.106:5000"
        registry_credentials = "registry-auth"
    }
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:3.8.12-buster'
                    args '-u root:root'
                }
            }
            steps {
                // sh 'pip install -r requirements.txt'
                sh 'pip install pyinstaller'
                sh 'pyinstaller -w -F test.py'
                stash(name: 'built-binary', includes: 'dist/test')
            }
            post {
                success {
                    archiveArtifacts "dist/test"
                }
            }
        }

        stage('Build-Image') {
            agent any
            steps {
                script {
                    app = docker.build 'jclee/jclee'
                }
            }
        }

        stage('Push-Image') {
            agent any
            steps {
                script {
                    // docker.withRegistry("https://registry.atg.re.kr", "registry-auth") {
                    docker.withRegistry("https://218.155.189.106:5000", "registry-auth") {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }

        // stage('Deploy') {
        //     agent any
        //     steps {
        //         sshagent(credentials: ['cj-ssh']) {
        //             sh '''
        //             ssh -t -t atgadmin@121.190.12.101 -o StrictHostKeyChecking=no -p 10022 "docker login registry.atg.re.kr --username atgregistry --password atg110810! && docker pull registry.atg.re.kr/cj-bio/recognition && docker rm -f recognition || true && docker run --rm -d -v /home/atgadmin/log:/log --name recognition registry.atg.re.kr/cj-bio/recognition"
        //             '''
        //         }
        //     }
        // }
    }
}
