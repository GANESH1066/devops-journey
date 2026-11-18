# Kubernetes (Minikube) Deployment
- Installed Minikube and kubectl.
- Configured Minikube to use the Docker container runtime.
- Built the Docker image directly inside the Minikube environment.
- Created a Kubernetes Deployment (`deployment.yaml`) with 1 replica.
- Created a NodePort Service (`service.yaml`) to expose the app.
- Successfully deployed the Python app and verified it using `kubectl port-forward` and `curl`.
