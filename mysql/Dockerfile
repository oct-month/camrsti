FROM mysql:8-debian
LABEL maintainer="ablocker ablocker@163.com"

ENV MYSQL_ROOT_PASSWORD=camrsti
ENV MYSQL_DATABASE=camrstidb

COPY ./camrstidb.sql /root/

CMD ["mysql -uroot -pcamrsti < /root/camrstidb.sql"]


EXPOSE 3306
VOLUME [ "/var/lib/mysql" ]
