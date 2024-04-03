FROM python:3/alpine

RUN pip install poetry

RUN poetry config vitrualenvs.create false

WORKDIR /workspace

COPY . /workspace

RUN poetry install

#CMD bots cenas