```bash
chmod +x run.sh
./run.sh
```
```bash
curl -vvv -x socks5h://localhost:1080 $(python3 -c "print(('A'*10000), end='')")
```

