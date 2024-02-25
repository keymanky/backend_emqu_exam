FROM python:3.10

RUN mkdir /backend_emqu_exam

WORKDIR /backend_emqu_exam

COPY requirements.txt /backend_emqu_exam

RUN pip install -r requirements.txt

COPY . /backend_emqu_exam

CMD [ "python", "./app.py" ]