## formas de correr docker-compose

### Default
docker-compose up -d

### Escalando
docker-compose up -d --scale node=3

### Ejemplos
http://0.0.0.0:5555/node/static
http://0.0.0.0:5555/node_replicado/static
http://0.0.0.0:5555/gunicorn/static