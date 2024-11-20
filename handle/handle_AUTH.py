

# handle AUTHENTICATE

from base64 import b64encode


def handle(client,msg):

    if msg['PAR'] == ['+']:

        authstr = '\0' + client.profile['REG_NICK'] + '\0' + client.profile['SASL_PWD']

        authenc = authstr.encode('ascii')

        authb64 = b64encode(authenc)

        authstr = authb64.decode('ascii')

        client.sock_send( ['AUTHENTICATE', authstr] )
