FROM python:3.9.4-slim

# set work directory
WORKDIR /src

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt /src/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /src/requirements.txt \
    && rm -rf /root/.cache/pip

# copy project
COPY . ./src
CMD ["uvicorn", "main:app","--reload", "true","--host", "0.0.0.0", "--port", "80"]