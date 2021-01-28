FROM python:3.9

LABEL maintainer="Hidetomo Shimaoka <hidetomo0102@asst.jxpress.net>"

ADD . ./

# install
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install

# app
EXPOSE 8080
CMD ["python", "app.py"]