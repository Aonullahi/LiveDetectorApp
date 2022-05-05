FROM python:3.6-slim-buster

RUN apt-get update -y --no-install-recommends

# gcc compiler and opencv prerequisites
RUN apt-get -y --no-install-recommends install nano git build-essential libglib2.0-0 libsm6 libxext6 libxrender-dev
RUN apt-get update && apt-get install -y --no-install-recommends \
	python3-opencv ca-certificates python3-dev git wget sudo  \
	cmake ninja-build && \
  rm -rf /var/lib/apt/lists/*

# tensorflow2.1
RUN pip install tensorflow==2.1.0 --no-cache-dir
RUN pip install cython

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 80

CMD python app.py
