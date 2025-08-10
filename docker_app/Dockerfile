FROM python:3.10

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY . /code

EXPOSE 8000

CMD ["bash", "-c", "uvicorn main_app:app --host 0.0.0.0 --port ${PORT:-8000}"]