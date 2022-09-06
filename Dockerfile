FROM ubuntu

RUN apt update
RUN apt install python3-pip -y
RUN pip3 install Flask pybase64 pandas numpy Flask-Cors paddleocr Pillow

WORKDIR /app

# We copy all
COPY . .

CMD [ "python3", "-m", "flask", "run","--host=0.0.0.0" ]
