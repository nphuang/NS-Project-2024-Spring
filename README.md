docker build -t socks5-server .

docker run -d -p 1080:1080 --name socks5-server socks5-server

docker stop socks5-server	

docker rm socks5-server

docker rmi socks5-server
