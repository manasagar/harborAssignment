FROM python:3.13-slim

WORKDIR /app
COPY input.txt /app/input.txt
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*


