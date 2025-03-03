FROM python:3.12-slim
WORKDIR /app
COPY pyproject.toml .
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --no-root

COPY . .
COPY .env .env

RUN mkdir -p /app/media
RUN mkdir -p /app/static

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
