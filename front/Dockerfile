FROM node:lts-alpine as builer

# RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories
# RUN apk update

RUN yarn config set registry https://repo.nju.edu.cn/repository/npm/
ENV NODE_ENV=product

WORKDIR /camrsti-front
COPY ./ /camrsti-front

RUN yarn && yarn build
RUN yarn cache clean


FROM nginx:stable-alpine
LABEL maintainer="ablocker ablocker@163.com"

COPY ./nginx/conf/nginx.conf /etc/nginx/nginx.conf
# COPY ./nginx/keys/nginx.crt /etc/nginx/cert/nginx.crt
# COPY ./nginx/keys/nginx_nopass.key /etc/nginx/cert/nginx.key

COPY --from=builer /camrsti-front/dist/ /usr/share/nginx/html/

EXPOSE 80
