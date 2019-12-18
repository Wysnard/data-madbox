run:
	docker pull lppier/docker-prophet
	docker-compose up -d --build

stop:
	docker-compose down