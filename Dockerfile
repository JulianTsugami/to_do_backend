FROM python:3.10
WORKDIR /to_do
COPY requirements.txt /to_do/
RUN pip install -r requirements.txt
COPY . /to_do/
