FROM python:3.9
WORKDIR /usr/local/app
COPY ./backend /usr/local/app/backend
RUN pip install -r ./backend/requirements.txt
ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", "--port", "8000", "backend:app" ]