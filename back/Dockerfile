FROM python:3.10-alpine
LABEL maintainer="ablocker ablocker@163.com"

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.cloud.tencent.com/g' /etc/apk/repositories
RUN apk update
RUN apk add --no-cache build-base musl-dev mysql-dev

WORKDIR /camrsti-back
COPY ./ /camrsti-back/

RUN pip install -i https://mirrors.cloud.tencent.com/pypi/simple -r requirements.txt --no-cache-dir

EXPOSE 8081

ENTRYPOINT ["python", "-u", "app.py"]
