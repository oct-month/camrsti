docker-compose up -d --build
timeout /t 5
docker cp ./mysql/camrstidb.sql camrsti-mysql:/root/
timeout /t 20
docker exec -i camrsti-mysql sh -c "exec mysql -uroot -pcamrsti < /root/camrstidb.sql"
