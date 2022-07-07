FROM python:3.10.5
WORKDIR /code
COPY ./requeriments.txt /code/requeriments.txt
RUN pip install --no-cache-dir --upgrade -r /code/requeriments.txt
COPY ./.env /code/.env
COPY ./utils /code/utils
COPY ./main.py /code/
COPY ./ClientWebSocket.py /code/ClientWebSocket.py
CMD ["uvicorn", "main:app","--ws","websockets","--host", "0.0.0.0", "--port", "6000", "--log-level","debug"]