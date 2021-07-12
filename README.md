# ethereum-block-finder

This is an application for getting details about blocks and transactions.

# Environment Setup

1. First you need to make sure that you have docker installed

2. Build the images by running `docker-compose build`

3. Run the containers by running `docker-compose up`

4. The swagger docs can be accessed by opening `localhost:500/docs/` on the browser

# API ENDPOINTS

There are two endpoints on this application

1. `/block/<number>/` -> number can either be a block number or `latest`

This endpoint returns details about a block. The block number is a decimal number or a string `latest`


2. `/block/<number>/txs/<txs>/` -> `number` is a block number or `latest` while `txs` is a transaction hash or index number

This is used to get information about a transaction on the blockchain.


# Testing

The app tests can be tested using `pytest`

To test,  you need to run bash from the docker container

1. check for running docker containers by running `docker ps`

2. find the Container ID of `ethereumblockfinder_server`

3. Run the bash for the container by running `docker exec -it <containerId> /bin/bash`

4. Now we are in the container's bash, we can test. To test, simply run `pytest`

If the tests passes, we should see a message stating the tests has passed.


# Technologies used

- Flask is the back-end framework used for the application
- Docker for containerizing
- Redis for Caching


# Developed by

This application was developed by Abdulmateen Tairu. 
 
