#!/bin/bash

docker build -t curl-exploit .
docker run --rm -it curl-exploit
docker system prune -f

