

# handle user KEEPALIVE

from time_calc import now
from keepalive import keepalive


def handle(client, kb_args):

    print( now() , 'OK:' , 'starting a `keep-alive` Thread() …' )

    keepalive(client)

