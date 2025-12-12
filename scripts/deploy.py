import time
import subprocess
import sys
import requests

CONTAINER_NAME = "my-app-container"
IMAGE_NAME = "my-app:latest"
PORT = 5000

def run_command(command):
    try:
        subprocess.check_call(command, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {command}")
        return False
    return True

def deploy():
    print(f"Deploying {IMAGE_NAME}...")
    
    print("Stopping old container...")
    run_command(f"docker stop {CONTAINER_NAME}")
    run_command(f"docker rm {CONTAINER_NAME}")

    print("Starting new container...")
    if not run_command(f"docker run -d --name {CONTAINER_NAME} -p {PORT}:5000 {IMAGE_NAME}"):
        print("Failed to start container.")
        sys.exit(1)

    print("Waiting for health check...")
    retries = 10
    url = f"http://localhost:{PORT}/health"
    
    for i in range(retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print("Health check passed! Deployment successful.")
                return
        except requests.ConnectionError:
            pass
        
        print(f"Health check attempt {i+1}/{retries} failed. Retrying in 2s...")
        time.sleep(2)

    print("Health check failed! Initiating rollback...")
    rollback()
    sys.exit(1)

def rollback():
    print(f"Stopping broken container {CONTAINER_NAME}...")
    run_command(f"docker stop {CONTAINER_NAME}")
    print("Rollback complete (container stopped). In a real environment, we would revert to the previous image tag.")

if __name__ == "__main__":
    deploy()
