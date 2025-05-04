run_basic:
	docker compose  -f ./Basic/docker-compose.yml  up --build

stop_basic:
	docker compose -f ./Basic/docker-compose.yml down

run_grad:
	docker compose -f ./Graduate/docker-compose.yml up --build

stop_grad:
	docker compose -f ./Graduate/docker-compose.yml down

run_grad_all:
	docker compose -f ./Graduate/docker-compose_all_mod.yml up --build

stop_grad_all:
	docker compose -f ./Graduate/docker-compose_all_mod.yml down


restart_basic: stop_basic run_basic

restart_grad: stop_grad run_grad