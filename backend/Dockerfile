FROM python:3.9
COPY . /app
WORKDIR /app
RUN python -m pip install poetry
RUN python -m poetry config virtualenvs.create false
RUN python -m poetry install --no-dev --no-ansi
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]