FROM python:3.10.5
WORKDIR /code
COPY ./routes /code/routes
COPY ./utils /code/utils
COPY ./.env /code/.env
COPY ./requeriments.txt /code/requeriments.txt
COPY ./main.py /code/

RUN pip install --no-cache-dir --upgrade -r /code/requeriments.txt

EXPOSE 3000

CMD ["uvicorn", "main:app","--ws","websockets", "--host", "0.0.0.0", "--port", "3000"]


