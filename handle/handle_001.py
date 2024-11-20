

# handle 001 (RPL_WELCOME)

from copy import deepcopy
from time_calc import dt_now
from server_dump import server_dump
from time import sleep
from rand_stuff import randnum


def handle(client, msg):

    # you are now registered

    client.registered = dt_now()


    # nick and servername

    client.myserv = deepcopy(msg['SRC'])

    client.mynick = deepcopy(msg['PAR'][0])


    # dump server information

    server_dump(client)


    # auto commands

    ct  = randnum(6)

    for cmd in client.profile['AUTO_CMD']:

        if cmd.upper().startswith('JOIN '): sleep(1)

        cmd = cmd.replace('&me', client.mynick)
        cmd = cmd.replace('&ct', ct)

        client.sock_send( cmd )

