docker-compose up -d --build
docker cp ./mysql/camrstidb.sql camrsti-mysql:/root/
docker exec -i camrsti-mysql sh -c "exec mysql -uroot -pcamrsti < /root/camrstidb.sql"
