```
> amd64 compatible

docker build \
--platform linux/amd64 \
-t michalsw/inspector:latest .


docker run --rm -d --name inspector michalsw/inspector:latest
docker exec -it inspector sh
docker stop inspector


kubectl run inspector \
--image michalsw/inspector:latest \
--restart=Never --command -- sleep infinity

kubectl exec -it inspector -- /bin/sh


> or you can always run alpine and install packages
docker run -it alpine:latest sh
```
