FROM python:3.11-slim-bookworm
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app
COPY pyproject.toml README.md LICENSE /app/
COPY src /app/src
COPY portshield /app/portshield
RUN pip install --no-cache-dir . && useradd --uid 10001 --create-home appuser
COPY data/public /app/data/public
USER 10001
EXPOSE 8000
CMD ["uvicorn", "portshield_ai.api:app", "--host", "0.0.0.0", "--port", "8000", "--no-access-log"]
