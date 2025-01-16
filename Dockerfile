FROM python:3.9

# системные пакеты 
RUN apt-get update && apt-get install -y \
    libpq-dev gcc netcat-openbsd


WORKDIR /file_sharing

COPY requirements.txt /file_sharing/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /file_sharing/

RUN chmod +x /file_sharing/entrypoint.sh

EXPOSE 8000
ENTRYPOINT ["/file_sharing/entrypoint.sh"]
