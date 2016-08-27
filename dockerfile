FROM python:3.5.1
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
add . /code/
RUN cat /code/docker_entrypoint.sh
ENTRYPOINT ["/code/docker_entrypoint.sh"]
