## Pysocksproto
A library for creating your own programs on SOCKS proto

### Examples
Open a simply socks server 
```
import pysocksproto
hs = pysocksproto.socksServer("0.0.0.0", 4545, pysocksproto.socksThread)
hs.serve()

```

To support BIND command, you have to specify ipv4 or ipv6 bind adresses
```
hs.set_bind_addresses("0.0.0.0", None)
```

To support username/password auth
```
hs = pysocksproto.socksServer("0.0.0.0", 
                            4545,  
                            pysocksproto.socksThread,    
                            require_auth=True, 
                            valid_creds={"username":"passw0rd", "u2":"p2"})

```

Or override verify_creds method in socksThread, for your own verification method
```
class custom(pysocksproto.socksThread):
    def verify_creds(self, username:str, password:str):
        if random.randint(0, 2) == 1:
            return True
        return False

hs = pysocksproto.socksServer("0.0.0.0", 4545, custom, require_auth=True)
hs.serve()      
```


You can use methods stored in Tools class, methods that start with "server" - provide server functionality, with "client"  - client functionality.

For example, use your own CONNECT method - allow connect only to specific adresses

```
class custom(pysocksproto.socksThread):
    def connect_request_handler(self, version:int, cmd:int, atype:int, target_address:str, target_port:int):
        allowed = ['12.34.56.78', '11.22.33.44']
        resolved = target_adress
        if atype == pysocksproto.ATYP_DOMAINNAME:
            resolved = socket.gethostbyname(resolved)
        if not resolved in allowed:
            pysocksproto.Tools.serverSendCmdResp(self.conn, 
                                    version, 
                                    pysocksproto.REPCODE_FORBIDDEN, 
                                    atype, 
                                    target_adress, 
                                    target_port)
            return
        super().connect_request_handler(version, cmd, atype, target_address, target_port)

hs = pysocksproto.socksServer("0.0.0.0", 4545, custom)
hs.serve()      
```
### Bind a port on socks proxy
class socksBind - for creating BIND requests to socks servers. 
Example:
```
import ysocksproto

cl = pysocksproto.socksBind("132.232.14.30", 	33221)
_, address, port = cl.BindProxyPort()
print(f"Proxy bound a port {port} on {address}")
_, address2, port2 = cl.WaitProxyBindConnect()
print(f"Someone connected to proxy from {address2}:{port2}")
cl.conn.send(b"hello, baby\n")
print(cl.conn.recv(10))
```
If you want to redirect connection to bound port on your system, use
```
cl.CreateProxyRedirection("127.0.0.1", 4444)
```
Program will connect to 127.0.0.1:4444, and then resend all data from proxy connection to 127.0.0.1 and back