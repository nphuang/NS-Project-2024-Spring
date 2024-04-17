#!/bin/bash

docker build . -t env

docker run --rm -it --net="host" -t env

docker rmi env
