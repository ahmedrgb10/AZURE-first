FROM python:3.10.7-slim-buster
WORKDIR /app
COPY . /app/
RUN pip3 install -r requirements.txt
EXPOSE 5050
CMD [ "python","webapp.py" ]
