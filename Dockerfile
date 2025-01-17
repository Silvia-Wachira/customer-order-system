# pull official base image
FROM python:3.10-alpine
# set work directory
WORKDIR /app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# install psycopg2 dependencies
RUN apk update \
 && apk add postgresql-dev gcc python3-dev musl-dev
# install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

# Expose port 8080
EXPOSE 8080

CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8080"]