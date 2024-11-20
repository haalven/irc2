

# handle bot_TIME

from time_calc import dt_now


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:

        client.sock_send( ['NOTICE', msg['NICK'], ':'+str(dt_now())] )
