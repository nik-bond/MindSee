FROM python:3.10.6-buster

WORKDIR /staging

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY api api
COPY setup.py setup.py

CMD uvicorn api.fast:app --host 0.0.0.0 --port $PORT

#COPY mindsee mindsee
#COPY setup.py setup.py
#RUN pip install .

#RUN pip install --upgrade pip
#COPY Makefile Makefile
#RUN make reset_local_files

