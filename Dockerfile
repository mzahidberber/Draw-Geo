FROM python:3

RUN apt-get update

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENV ALLOWED_HOSTS=$ALLOWED_HOSTS
ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG

WORKDIR /geo