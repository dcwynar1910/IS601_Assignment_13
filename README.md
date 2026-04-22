# Module 13

In order to run locally git clone the repo and run the command to get this working on your machine
docker compose up --build

To run tests once docker is up and running use: 
docker-compose exec --user root web pytest --cov=app --cov-report=term-missing
This shows the coverage as well as if anything is failing.

DockerHub Link: https://hub.docker.com/r/dcwynar1910/601_module13/tags