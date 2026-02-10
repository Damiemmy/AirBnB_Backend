FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y netcat-openbsd


WORKDIR /usr/src/djangobnb_backend

COPY ./requirements.txt /usr/src/djangobnb_backend/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /usr/src/djangobnb_backend/requirements.txt
COPY ./entrypoint.sh /usr/src/djangobnb_backend/entrypoint.sh
RUN sed -i 's/\r$//g' /usr/src/djangobnb_backend/entrypoint.sh
RUN chmod +x /usr/src/djangobnb_backend/entrypoint.sh

COPY . .

EXPOSE 8000

ENTRYPOINT ["/usr/src/djangobnb_backend/entrypoint.sh"]
