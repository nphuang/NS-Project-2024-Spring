FROM alpine:latest

RUN apk --no-cache add dante-server

COPY sockd.conf /etc/

EXPOSE 1080

CMD ["sockd", "-f", "/etc/sockd.conf", "-N", "1"]