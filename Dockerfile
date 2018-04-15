FROM python:2.7.10
ADD . /machine-learning1
WORKDIR /machine-learning1
RUN pip install --upgrade pip
RUN pip install -r requirements.txt