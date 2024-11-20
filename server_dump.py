
# save server data

from socket import gethostbyaddr
from time import time
from json import dump


def server_dump(client):

    # the data
    addr = client.profile['CON_ADDR']
    port = client.profile['CON_PORT']

    try: realsvraddr = client.ircsock.getpeername()[0]
    except Exception: realsvraddr = None
    try: realsvrname = gethostbyaddr(realsvraddr)[0]
    except Exception: realsvrname = None

    tls    = client.profile['CON_ENCR']
    cipher = client.ircsock.cipher() if tls else False

    myserv = client.myserv

    # the short dump
    svr_dump = {
        'CON_ADDR':     (addr, port),
        'REAL_ADDR':    (realsvraddr, realsvrname),
        'TLS_CIPHER':   cipher,
        'SVR_NAME':     myserv
    }

    # the file
    svrfile =  client.ircpath + '/servers/'
    svrfile += str(time()) + '-' + client.profilename + '-connection.json'

    # write
    with open(svrfile, 'w') as f: dump(svr_dump, f, indent=2)
