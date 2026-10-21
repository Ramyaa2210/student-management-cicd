# Student Management CI/CD Demo

A small Flask application for an Agile Process Development and DevOps assessment using GitHub, Jenkins, Docker, and Kubernetes.

## Files

- `app.py`: Flask student portal and JSON endpoints
- `test_app.py`: automated unit tests
- `requirements.txt`: application dependencies
- `Dockerfile`: container image instructions
- `Jenkinsfile`: Jenkins pipeline
- `kubernetes/deployment.yaml`: two-replica Kubernetes Deployment
- `kubernetes/service.yaml`: NodePort Service on port 30080

## Run locally

Install Python 3.12 or later, then run:

```powershell
py -m pip install -r requirements-dev.txt
py -m pytest -v
py app.py
```

Open `http://localhost:5000`.

## Build and deploy manually

Run these commands from the project folder with Docker Desktop and the Docker Desktop Kubernetes cluster running:

```powershell
docker build -t student-management-cicd:latest .
kubectl apply -f kubernetes/deployment.yaml
kubectl apply -f kubernetes/service.yaml
kubectl rollout status deployment/student-management
kubectl get pods
```

Open `http://localhost:30080`.

## Jenkins notes

The included Jenkinsfile uses Windows `bat` steps and expects the Jenkins agent to have Python (`py`), Docker CLI/engine, `kubectl`, and access to the Docker Desktop Kubernetes context. If Jenkins runs as a Windows service account, ensure that account has access to Docker and the intended kubeconfig/context before running the pipeline.

This demo builds a local image; it does not push to a remote image registry. Docker Desktop Kubernetes can use the locally built image. For a remote Kubernetes cluster, publish the image to a registry and update the Deployment image reference.
