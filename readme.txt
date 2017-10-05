### run

```
docker build --tag verificator .
docker run -d --rm -it -p 80:8080 -v `pwd`/uuids:/opt/code/uuids --name verificator verificator
```
