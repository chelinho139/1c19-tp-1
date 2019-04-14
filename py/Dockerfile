FROM python:2.7.10

WORKDIR /usr/src/app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 4000

CMD [ "gunicorn", "-b", ":4000", "app:app" ]