# Makefile

# CONFIG
PI_USER=pi
PI_HOST=raspberrypi.local   # or IP like 192.168.1.100
PI_PROJECT_DIR=/home/pi/smart_home
LOCAL_PROJECT_DIR=.

SSH=$(PI_USER)@$(PI_HOST)

deploy:
	rsync -avz --exclude '__pycache__' --exclude '.venv' $(LOCAL_PROJECT_DIR)/ $(SSH):$(PI_PROJECT_DIR)

run:
	ssh $(SSH) "cd $(PI_PROJECT_DIR) && python3 main.py"

deploy-run: deploy run
