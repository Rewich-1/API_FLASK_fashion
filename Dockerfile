FROM python:3.9-buster

WORKDIR /project 

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /project

EXPOSE 5000

ENTRYPOINT ["python"]
CMD ["app.py"]
