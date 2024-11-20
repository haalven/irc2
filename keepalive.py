
# ping server every x seconds to keep alive
# start with `keepalive(client)`

import threading
from time import sleep


def keepalive(client):

    def keepalive_thread(client):
        while 1:
            sleep(60)
            try: client.sock_send([ 'PING', 'keep-alive' ])
            except Exception: return None

    ka = threading.Thread(target=keepalive_thread, args=(client,))

    ka.daemon = True

    ka.start()
