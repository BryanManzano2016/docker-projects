FROM python:3.9-alpine

WORKDIR /api-flask

COPY . .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "main.py"]
