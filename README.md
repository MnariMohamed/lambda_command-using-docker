#steps to deploy the image to aws

1- run: aws ecr get-login-password --region eu-west-3 | docker login --username AWS --password-stdin 453046496729.dkr.ecr.eu-west-3.amazonaws.com

2- run from terminal in this directory: docker build -t mysqldump .

3- run: docker tag mysqldump:latest 453046496729.dkr.ecr.eu-west-3.amazonaws.com/mysqldump:latest

4- run: docker push 453046496729.dkr.ecr.eu-west-3.amazonaws.com/mysqldump:latest

5- go to the created lambda in AWS and attach the pushed image
