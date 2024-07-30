FROM python:3.10

WORKDIR /app/

RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry

COPY ./pyproject.toml ./poetry.toml ./poetry.lock* README.md /app/

RUN poetry install --no-root

COPY ./example/ /app/example

RUN poetry install

ENTRYPOINT ["poetry", "run"]