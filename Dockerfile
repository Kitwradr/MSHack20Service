FROM python:3.6.8

WORKDIR /app
COPY . /app

RUN apt update

RUN pip install -r requirements.txt

EXPOSE 5001

RUN chmod -x main.py ;
CMD ["python", "main.py"]