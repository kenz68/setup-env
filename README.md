
## Start zookeeper & kafka

`docker-compose up -d`

## Test services are running

`docker ps`

## Create Kafka Topic

`docker exec setup-env-kafka-1 kafka-topics --create --topic invoices --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1`

### `docker ps` to check `setup-env-kafka-1`

## Check Kafka logs

`docker-compose logs kafka`

## Start Producer

`docker exec -it setup-env-kafka-1 kafka-console-producer --topic invoices --bootstrap-server localhost:9092`

## Send a mesage

`>Hello Kafka!` then check the message on `Offset Explorer`