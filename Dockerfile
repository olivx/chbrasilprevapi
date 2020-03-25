FROM python:3.7.3-slim-stretch


ENV WORKERS="1"
ENV DEBUG="True"
ENV LOG_LEVEL="INFO"
ENV ALLOWED_HOSTS="127.0.0.1, .localhost, *"
ENV SECRET_KEY="!8z6x+11-&vp3f+uy37&cur^wv&-l4v5vd+*)2pqzea=)a%++w"
ENV SECRET_KEY="eb*xnd%dbcj*u0q^y75s!mz9)87(_i@vz&i@w4r-pc3rp1duf1"
ENV FILENAME_LOG_GUNICORN="/var/log/app/gunicorn.log"
ENV FILENAME_LOG_APP="/var/log/app/app.log"

WORKDIR /app

COPY Pipfile* /app/

RUN pip install --upgrade pip

RUN pip install pipenv && \
    pipenv install --system --deploy

RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser

RUN mkdir /var/log/app && chown appuser /var/log/app

COPY . /app

USER appuser

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "chbrasilprev.wsgi:application"]
