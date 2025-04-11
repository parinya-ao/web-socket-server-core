FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
COPY .env .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080
CMD ["python", "-u", "main.py", "server"]
