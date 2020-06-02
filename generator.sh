#!/bin/bash

REPOSITORY_NAME=$1
REPOSITORY_DESC=$2

echo "Cloning the template repository"
git clone https://github.com/vocacorg/terraform-provider-template.git

echo "Installing pre-reqs modules"
python3 installpreqs.py

echo "Preprocessing the target repository"
python3 preprocess.py $REPOSITORY_NAME $REPOSITORY_DESC

echo "Creating target repository"
python3 createrepo.py $REPOSITORY_NAME $REPOSITORY_DESC

cd $REPOSITORY_NAME
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/vocacorg/$REPOSITORY_NAME.git
git push -u origin master