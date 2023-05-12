# ML - Engineering Challenge

## High-level Architecture Diagram

![img.png](Architecture.png)

- The code is maintained on Github.
- When code is pushed to a branch, it triggers a Cloud Build trigger to build and push the image to Google's Container Registry. 
- After a successful push, the docker image is deployed as a service via Cloud Run which is Google's managed platform for running containers.
- The model is served as a Flask Restful API.

## How do I call the API?

Link to the api: 

## Repository Content

The repository has the following folders/files that are required to deploy the service:

- `model`           : Includes code for model that was provided with the challenge. 
- `Dockerfile`      : Includes instructions to build docker image.
- `main.py`         : Flask application script.
- `requirements.txt`: Python dependencies to be installed at the start of runtime.
- `setup.py`        : To package `model` module.

