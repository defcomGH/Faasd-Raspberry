# FROM python:3.7.14-alpine3.16

# WORKDIR /src

# ENV FLASK_APP app.py

# ENV FLASK_RUN_HOST 0.0.0.0

# EXPOSE 5000

# COPY requirements.txt requirements.txt 

# RUN pip install -r requirements.txt

# CMD ["python3", "app.py"]

FROM python:3.7.14-alpine3.16

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]