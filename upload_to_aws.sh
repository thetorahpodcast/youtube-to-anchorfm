aws ecr get-login-password --region il-central-1 | docker login --username AWS --password-stdin 992382515700.dkr.ecr.il-central-1.amazonaws.com
docker build -t torahpodcast-youtube-docker -f Dockerfile-custom .
docker tag torahpodcast-youtube-docker:latest 992382515700.dkr.ecr.il-central-1.amazonaws.com/torahpodcast-youtube-docker:latest
docker push 992382515700.dkr.ecr.il-central-1.amazonaws.com/torahpodcast-youtube-docker:latest
