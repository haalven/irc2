
# connect client.ircsock object

import socket, ssl
from keepalive import keepalive
from time_calc import dt_now, now
from xterm_control import color, endcol, clear


def sockconnect(client):

    # socket parameters

    addr, port = client.profile['CON_ADDR'], client.profile['CON_PORT']

    socket.setdefaulttimeout(client.profile['CON_TOUT'])


    # "client.ircsock" object

    if client.profile['CON_ENCR']:

        encrypted = ssl._create_unverified_context()

        plain = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        client.ircsock = encrypted.wrap_socket(plain, server_hostname=addr)


    else: # plain socket

        print(now(), '***', color(196) + 'THIS CONNECTION IS NOT ENCRYPTED!' + endcol(), '***')

        client.ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    # connect

    print(now(),'*',f'connecting to {addr}:{port} ...')

    try: client.ircsock.connect((addr, port))

    except Exception as e:

        print('CONNECT ERROR:', str(e))

        return None

    except KeyboardInterrupt:

        print(clear(), 'INTERRUPTED .')

        return None

    # connection established

    client.connected = dt_now()

    print(now(), '*', 'connected:', str(client.ircsock))

