FROM python:3.8.3

ADD productservice.py /

RUN pip install flask

ENV FLASK_APP ./productservice.py

EXPOSE 5000

CMD [ "flask", "run", "--host=0.0.0.0" ]
