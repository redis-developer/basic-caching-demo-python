
<div style="position: absolute; top: 0px; right: 0px;">
    <img width="200" height="200" src="https://redislabs.com/wp-content/uploads/2020/12/RedisLabs_Illustration_HomepageHero_v4.svg">
</div>

<div style="height: 150px"></div>

# NodeJS Redis Example

Show how the redis works with NodeJS, Express.

## Try it out

<p>
    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heorku" width="200px"/>
    <a>
</p>

<p>
    <a href="https://vercel.com/new/git/external?repository-url=https%3A%2F%2Fgithub.com%2FITsolution-git%2Fnode-express-redis&env=REDIS_ENDPOINT_URI,REDIS_PASSWORD&envDescription=REDIS_ENDPOINT_URI%20is%20required%20at%20least%20to%20connect%20to%20Redis%20clouding%20server" target="_blank">
        <img src="https://vercel.com/button" alt="Deploy with Vercel" width="200px" height="50px"/>
    </a>
</p>

<p>
    <a href="https://deploy.cloud.run" target="_blank">
        <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" width="200px"/>
    </a>
</p>


## How it works?

![How it works](docs/screenshot001.png)

## How to run it locally?

#### Setup and run frontend

```sh
cd client
npm install
npm run serve
```

### Run docker compose or install redis manually
```sh
docker network create global
docker-compose up -d --build
```

#### If you install redis manually open django-backend/configuration folder and copy `.env.example` to create `.env`. And provide the values for environment variables if you install redis manually
    - REDIS_HOST: Redis server host
    - REDIS_PORT: Redis server port
    - REDIS_DB: Redis server db index

#### Setup and run backend

``` sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
cd django-backend
python3 manage.py runserver 5000
```
