FROM python:2.7.10

#RUN mkdir /as
WORKDIR /usr/src/app

COPY . .
#COPY requirements.txt /as/requirements.txt

RUN pip install -r requirements.txt

#COPY / /as/src

EXPOSE 4000

#CMD [ "gunicorn", "--chdir", "src", "--pythonpath", "/as/src", "app:app", "-b", ":4000" ]
CMD [ "gunicorn", "-b", ":4000", "app:app" ]