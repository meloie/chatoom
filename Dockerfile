FROM python:3.6

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD source chat
CMD uvicorn chat.app:app --host 0.0.0.0
