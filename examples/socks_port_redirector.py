

import argparse
import pysocksproto
from pysocksproto import exceptions

def main():
    ps = argparse.ArgumentParser()
    ps.add_argument("socksIp",  type=str)
    ps.add_argument("socksPort", type=int)
    ps.add_argument("--localIp",   type=str, default="127.0.0.1", help="Local ip, which will handle incoming connection (default 127.0.0.1)")
    ps.add_argument("--localPort",  type=int, default="4455", help="Local port, which will handle incoming connection (default 4455)")
    ps.add_argument("--creds", type=str,  required=False, default="", help="auth creds, eg username:passw0rd")
    v = ps.parse_args()
    
    try:
        cl = pysocksproto.socksBind(v.socksIp, v.socksPort, logging=True, creds = v.creds)

        print("Trying to bind a port on "+v.socksIp )
        _, adress, port = cl.BindProxyPort()
        
        print(f"Binded ({v.socksIp}) a port on {adress}  {port}")
        
        print("Wait connection....")
        _, address, port = cl.WaitProxyBindConnect()
        
        print(F"Somneone connected from {address}, {port}")
        cl.CreateProxyRedirection(v.localIp, v.localPort)
    
    except exceptions.UnsuccessfulRepcode as e:
        if e.repcode == pysocksproto.REPCODE_CMD_NOT_SUPPORTED:
            print("CMD NOT SUPPORTED")
        elif e.repcode == pysocksproto.REPCODE_FORBIDDEN:
            print("CMD IS FORBIDDEN")
        else:
            print(f"Unknown repcode {e.repcode}")
        return

if __name__ =="__main__":
    main()