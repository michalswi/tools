```
docker build -t michalsw/inspector:latest .
docker run --rm -d --name inspector michalsw/inspector:latest
docker exec -it inspector sh
docker stop inspector
```
