![Fang - FastApi & Angular + Postgres](./resources/Fang%20-%20social%20media.png)

# [FastAPI](https://fastapi.tiangolo.com/) // [Angular](https://angular.io/) // [Postgres](https://www.postgresql.org/)

Inspired by [Aaron Bassett's](https://github.com/aaronbassett/) [FARM Stack](https://www.mongodb.com/developer/how-to/FARM-Stack-FastAPI-React-MongoDB/).


---

## Setup

```
cp ./sample.env ./.env
```

## Frontend

```shell
cd ./frontend
npm ci
npm run serve
```

## Backend

```shell
cd ./backend
python -m virtualenv .venv
./.venv/Scripts/activate.ps1
pip install -r requirements.txt
cd ..
python -m backend
```

## Docker

Dev

```shell
docker compose build
docker compose up -d
```

Prod

```shell
docker compose -f ./docker-compose.yml -f ./docker-compose.prod yml build
docker compose -f ./docker-compose.yml -f ./docker-compose.prod yml up -d
```
