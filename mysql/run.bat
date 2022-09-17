docker run -d --name camrsti-mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=camrsti -e MYSQL_DATABASE=camrstidb mysql:8-debian
timeout /t 5
docker cp ./camrstidb.sql camrsti-mysql:/root/
timeout /t 60
docker exec -i camrsti-mysql sh -c "exec mysql -uroot -pcamrsti < /root/camrstidb.sql"
