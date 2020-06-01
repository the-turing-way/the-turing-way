FROM ubuntu:bionic
RUN apt-get update \
	&& apt-get install -y python3 python3-pip \
	&& rm -rf /var/lib/apt/lists/*
RUN python3 -m pip install --upgrade pip setuptools wheel
COPY ./book/website/requirements.txt requirements.txt
RUN pip install -r requirements.txt
