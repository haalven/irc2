

# handle 903 (RPL_SASLSUCCESS)

from copy import deepcopy


def handle(client,msg):

    if not client.registered:

        client.sasl_nick = deepcopy( msg['PAR'][0] )

        client.sock_send(['CAP','END'])
