FROM python:3.7

COPY requirements.txt /tmp/requirements.txt

RUN mkdir /app && pip3 install -r /tmp/requirements.txt

COPY app.py /app/app.py

ENTRYPOINT ["python3"]
CMD ["/app/app.py"]
