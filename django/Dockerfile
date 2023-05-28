FROM python:3.11

WORKDIR /data

COPY requirements.txt .

RUN pip install -r requirements.txt

RUN pip install psycopg2-binary --force-reinstall --no-cache-dir

COPY . .

EXPOSE 8000

#CMD python manage.py runserver 0.0.0.0:8000