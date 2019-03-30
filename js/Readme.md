## como correr la imagen

docker build -t doritos/node-web-server .
docker run -p 48000:3000 -d doritos/node-web-server
curl localhost:48000