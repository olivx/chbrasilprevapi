FROM python:3.7.3-slim-stretch


WORKDIR app

COPY Pipfile* ./

RUN pip install --upgrade pip

RUN pip install pipenv && \
    pipenv install --system --deploy


RUN mkdir /var/log/app


COPY . /app


EXPOSE 8000
ENTRYPOINT ["sh", "/app/entrypoint.sh"]
# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "chbrasilprev.wsgi:application"]
