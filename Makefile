run:
	docker compose up --build

stop:
	docker compose down


restart: stop run