

# handle user LAG

from time import time


def handle(client, kb_args):

    client.sock_send([ 'PING' , 'time=' + str(time()) ])

