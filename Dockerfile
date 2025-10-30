FROM python:3.11-slim

WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]