FROM python:3.9-alpine

WORKDIR /api-flask

COPY . .

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

ENTRYPOINT [ "flask", "--app", "main", "run", "--host", "0.0.0.0"]
