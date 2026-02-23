FROM python:3.12-slim-bookworm

COPY DS-Project-1-PU-AIDS-2024-28 /app

RUN apt-get update && apt-get -y upgrade && apt-get -y install python3-pip

WORKDIR /app

RUN pip3 install -r requirements.txt --no-cache-dir

RUN chmod +x start-backend-frontend.sh

CMD ["bash", "start-backend-frontend.sh"]
