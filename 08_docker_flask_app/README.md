# Docker Use Case: Dockerized Flask Application

## Objective

To demonstrate Docker by containerizing a simple Flask web application and running it inside a Docker container.

## Tool Used

Docker

## Files

- app.py
- requirements.txt
- Dockerfile

## Application Routes

### Home Page

```text
http://localhost:5000
```

### Status API

```text
http://localhost:5000/api/status
```

## Installation Requirement

- Docker Desktop
- Python
- Flask

## Local Execution Command

```bash
python app.py
```

## Docker Build Command

```bash
docker build -t docker-flask-app .
```

## Check Docker Images

```bash
docker images
```

## Docker Run Command

```bash
docker run -d -p 5000:5000 --name flask-container docker-flask-app
```

## Check Running Containers

```bash
docker ps
```

## Testing URL

```text
http://localhost:5000
```

## Testing API URL

```text
http://localhost:5000/api/status
```

## Sample JSON Output

```json
{
  "application": "Docker Flask App",
  "message": "Flask app is running successfully inside Docker container",
  "status": "running"
}
```

## Stop Container

```bash
docker stop flask-container
```

## Remove Container

```bash
docker rm flask-container
```

## Conclusion

This use case demonstrates how Docker can be used to package and run a Flask application inside a container.