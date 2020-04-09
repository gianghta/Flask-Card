FROM python:3.7.6-buster
LABEL maintainer "Giang Ta <tagh@mail.uc.edu>"
ADD . /project_flask_card
WORKDIR /project_flask_card
RUN pip install poetry
RUN poetry export --without-hashes  -f requirements.txt > requirements.txt
RUN pip install --no-cache-dir -r requirements.txt