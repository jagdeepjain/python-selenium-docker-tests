import os.path
import subprocess
from subprocess import PIPE

import time

def start():
    p = subprocess.Popen(['docker-compose', '-p ui_test', 'up', '-d'])
    time.sleep(5)
    p.wait()
    print("docker started....")

def stop():
    p = subprocess.Popen(['sh', './clean.sh'])
    time.sleep(5)
    p.wait()

start_docker()
clean_docker_container()

