ROOT_DIR := excidium

help: ## Show this help message (default)]
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-20s\033[0m \033[35m%s\033[0m\n", $$1, $$2}' $(MAKEFILE_LIST)

run: ## DEV : run locally
	echo "run locally, uncomment what you need in the Makefile"
	#npm start # angular
	#npm install --prefix app # nodejs
	#npm start --prefix app # nodejs
	pip install --user -r app/requirements.txt
	python app/app.py # python
	#gunicorn --workers=2 --bind=0.0.0.0:5000 --chdir app app:app # python-flask

cleanup: ## DEV : cleanup
	echo "install locally"
	#rm -rf something

install: ## DEV: install locally
	echo "install locally"
	echo "TO IMPLEMENT"

docker: ## DEV DOCKER: running docker
	echo "running docker locally, change docker run to docker run -p ***:*** if you need network capabilities"
	docker build -t "$(ROOT_DIR)" .
	docker run "$(ROOT_DIR)"

docker-daemon: ## DEV DOCKER: daemonize your docker container to the local system
	echo "running docker locally, change docker run to docker run -p ***:*** if you need network capabilities"
	docker build -t "$(ROOT_DIR)" .
	docker run -d --restart=always --name="$(ROOT_DIR)" "$(ROOT_DIR)"

docker-cleanup: ## DEV DOCKER : docker cleanup
	echo "stop docker container and remove the image so the app name can be used again"
	docker stop "$(ROOT_DIR)"
	docker rm "$(ROOT_DIR)"
