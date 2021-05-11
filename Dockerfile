FROM python:3.8-slim-buster

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

RUN pytest -v --junitxml=reports/result.xml

COPY . /app

EXPOSE 5000

ENTRYPOINT ["python3"]

CMD ["app.py"]