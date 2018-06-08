FROM alpine:3.7

RUN apk add --update --no-cache python python-dev py-pip

WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "run-speedtest.py"]
