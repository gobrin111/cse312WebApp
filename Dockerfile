FROM python:3.12

ENV HOME /root
WORKDIR /root

COPY . .

RUN pip3 install Flask

EXPOSE 8080
CMD python3 -u app.py