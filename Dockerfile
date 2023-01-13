FROM python:3.8-slim-buster
WORKDIR /sources
COPY . /sources
EXPOSE 80
CMD ["python", "./MainScores.py"]
