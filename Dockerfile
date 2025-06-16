FROM python:3.12-slim

RUN pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock README.md ./

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY . .
COPY .env .env

# Ensure all dependencies are installed
RUN poetry install --no-interaction --no-ansi \
  && pip install loguru

# Verify installation
RUN pip list

# Ensure loguru is installed
RUN pip install loguru

EXPOSE 80

CMD ["python3", "main.py"]