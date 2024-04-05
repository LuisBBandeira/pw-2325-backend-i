
docker.build:
	docker-compose build --force-rm

docker.run:
	docker-compose up -d

install: 
	poetry install

activate: install
	poetry shell

start: activate
	bot start