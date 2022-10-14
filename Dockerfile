FROM python:alpine3.16

RUN mkdir /applications
WORKDIR "/applications"

RUN pip install --upgrade pip
ADD src/*.py /applications/

# CMD ["python", "p12.py"]