## como correr la imagen

docker build -t doritos/python-web-server .
docker run -p 4000:4000 -d doritos/python-web-server
curl localhost:4000