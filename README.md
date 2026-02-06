# Eks-end-to-end-deployment
Use AWS EKS service for Deployment 
---

## 🐍 Python Application
- Flask is used to handle game logic and routing
- The game state is managed server-side
- UI is rendered using HTML templates

---

## 🐳 Dockerization
The application is containerized using Docker to ensure consistency across environments.

### Dockerfile Highlights
- Uses lightweight `python:3.9-slim` image
- Installs dependencies via `requirements.txt`
- Exposes port 5000
- Runs Flask application using `CMD`

### Docker Commands Used
docker build -t python-2048-game .
docker run -p 5000:5000 python-2048-game

### Kubctl Commands used 
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl get pods
kubectl get svc

###Install using Fargate
eksctl create cluster --name demo-cluster --region us-east-1 --fargate


 