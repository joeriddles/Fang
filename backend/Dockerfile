FROM python:3.9 as base
WORKDIR /app
COPY ./backend/requirements.txt ./requirements.txt
RUN pip install -r ./requirements.txt
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", "--port", "8000", "backend:app" ]

FROM base as prod
COPY ./backend /app/backend
