FROM python:3.10
WORKDIR /backend
COPY requirements.txt /backend/
RUN pip install fastapi uvicorn
COPY . /backend/
