FROM python:3.9

LABEL maintainer="Hidetomo Shimaoka <hidetomo0102@asst.jxpress.net>"

# install
COPY poetry.lock pyproject.toml ./
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

# app
ADD . ./
EXPOSE 80
RUN python app.py