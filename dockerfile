FROM python:3.8

RUN apt upgrade -y

RUN apt update -y

RUN apt install libgtk-3-0 -y

RUN apt install libgstreamer-plugins-base1.0-0 -y

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["flet","entrypoint.py","-n","-w","--port","5000"]