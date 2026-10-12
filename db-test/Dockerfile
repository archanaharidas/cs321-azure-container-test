FROM python:3.12-slim

WORKDIR /app

COPY db-test/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY db-test/app.py app.py

EXPOSE 8080

CMD ["python", "app.py"]
