echo "open docker"
# open -na "Docker"
open --background -a Docker

while (!(docker ps | grep "CONTAINER ID"))
do
  echo "waiting for docker"
  sleep 5
done
echo "docker is up"

echo "run redis"
docker run -p 6380:6379 -d redis

echo "run postgres"
docker run -e POSTGRES_PASSWORD=postgres -e POSTGRES_USERNAME=postgres -e POSTGRES_DB=test_db -p 5430:5432 -d postgres

echo "poetry install"
poetry install

echo "run server"
poetry run python server.py