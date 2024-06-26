# app/Dockerfile

FROM python:3.11

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
build-essential \
curl \
software-properties-common \
git \
&& rm -rf /var/lib/apt/lists/*

RUN ls
RUN pip3 install -r requirements.txt

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "webapp.py", "--server.port=8901", "--server.address=0.0.0.0"]





