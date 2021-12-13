FROM python:3.8.2-buster

WORKDIR /usr/workspace

COPY requirements.txt ./

RUN cat requirements.txt | xargs -n 1 -L 1 pip install

CMD ["tail", "-f", "/dev/null"]
