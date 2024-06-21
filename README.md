[![Test](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/test.yml/badge.svg)](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/test.yml)
[![Build](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/build.yml/badge.svg)](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/build.yml)
[![Review](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/review.yml/badge.svg)](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/review.yml)
[![Merge](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/merge.yml/badge.svg)](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/merge.yml)
[![Deploy](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/deploy.yml/badge.svg)](https://github.com/RoscoArgus/SwEng-Group-24/actions/workflows/deploy.yml)
# Quickstart

### NOTE: Ensure you create a .env file for both 'backend' and 'frontend' folders containing the following variables:

``` 
API_KEY_GPT3_5_TURBO = *Your GPT 3.5 Turbo API key*
API_KEY_GPT4 = *Your GPT 4 API key*
``` 
<br>

# Run demo using Docker

Note: You need Docker installed and running.
You can download Docker from here: [Docker](https://www.docker.com/products/docker-desktop/)

## Run from your terminal:

Firstly, clone the repo, then

```
cd SwEng-Group-24
docker-compose up
```

After the server compiles, open [localhost](http://localhost:3000)

If you get an error of this type:

> Is the docker daemon running?

Open docker again

## Why use Docker containers?

- You don’t have to install npm and other dependencies to run the demos
- The docker container should work for everyone regardless of OS, installed packages, etc

<br>

# Run demo locally

## Prerequisites
- Node.js
- Some version of Conda

## Setup conda environment

```
conda create -n taxonomy-builder-app python=3.10
conda activate taxonomy-builder-app
```

## Clone repository and install dependencies:

```
git clone <repo>
```

### For Frontend:
```
cd SwEng-Group-24/taxonomy-builder-app/production-app/frontend
npm install
npm start
```
After the server compiles open [localhost](http://localhost:3000)


### For Backend (in a separate terminal):
```
cd SwEng-Group-24/taxonomy-builder-app/production-app/backend
pip install -r requirements.txt
uvicorn test_api:app --reload
```