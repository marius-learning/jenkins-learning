FROM python:3.8-slim-buster

LABEL app="flask"

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt

COPY . .

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0", "--port=8080"]

EXPOSE 8080