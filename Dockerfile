FROM python:3.8.5

WORKDIR /app

COPY app /app

RUN pip install flask

CMD ["python", "app.py"]