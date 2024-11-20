

# handle ERROR

from time_calc import now

def handle(client, msg):


    error_msg = '\x20'.join(msg['PAR']).lower()


    # do not auto-reconnect after being killed/banned

    if ('killed' in error_msg) \
        or ('banned' in error_msg) \
        or ('k-line' in error_msg) \
        or ('g-line' in error_msg) \
        or ('z-line' in error_msg):

            client.reconnect = 0

            print( now() , '*' , 'kill/ban -> reconnect has been disabled' )
