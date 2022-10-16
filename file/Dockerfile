FROM node:lts-alpine
LABEL maintainer="ablocker ablocker@163.com"

# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.cloud.tencent.com/g' /etc/apk/repositories
# RUN apk update

RUN yarn config set registry http://mirrors.cloud.tencent.com/npm/
ENV NODE_ENV=product

WORKDIR /camrsti-file
COPY ./ /camrsti-file/

RUN yarn
RUN yarn cache clean

EXPOSE 8082
VOLUME [ "/camrsti-file/public" ]

ENTRYPOINT [ "yarn", "serve" ]
