# echo_keepalive_python

### server
```
# keep alive
$ python3 server.py 8080 true 

# not keep alive
$ python3 server.py 8080 false
```

### client
```
# keep alive
$ python3 client.py 0.0.0.0 8080 true

# not keep alive
$ python3 client.py 0.0.0.0 8080 true
```

reference：https://kazuhira-r.hatenablog.com/entry/2020/02/27/002840
