FROM python:3.10.5
WORKDIR /code
COPY ./requeriments.txt /code/requeriments.txt
COPY ./middlewares /code/middlewares
COPY ./routes /code/routes
COPY ./config /code/config
COPY ./models /code/models
COPY ./.env /code/.env
COPY ./utils /code/utils
COPY ./main.py /code/
RUN pip install --no-cache-dir --upgrade -r /code/requeriments.txt

CMD ["uvicorn", "main:app","--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

