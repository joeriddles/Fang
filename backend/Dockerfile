ARG UID
ARG GID
ARG USERNAME

FROM python:3.9 as base
ARG UID
ARG GID
ARG USERNAME
ENV UID=$UID
ENV GID=$GID
ENV USERNAME=$USERNAME

ENV VIRTUAL_ENV=/opt/venv
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /app
COPY backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN groupadd --gid ${GID} group \
    && useradd --uid ${UID} --gid ${GID} --password --create-home ${USERNAME}
USER ${UID}:${GID}

ENTRYPOINT [ "uvicorn" ]
CMD [ "--host", "0.0.0.0", "--port", "8000", "backend:app" ]

FROM base as prod
COPY ./backend /app/backend
