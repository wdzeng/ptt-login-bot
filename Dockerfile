FROM python:3.10-alpine
RUN pip install --no-cache-dir PyPtt
COPY main.py /app/main.py

WORKDIR /app
ENTRYPOINT [ "python", "main.py" ]
LABEL description="Get shopee coins everyday."
