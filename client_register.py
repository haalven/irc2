
# send registration data

from rand_stuff import randnam, randnum


def client_register(client):

    if client.connected:

        # random stuff

        rnd = randnam(client)

        ct  = randnum(4)


        # replacements

        nick  = client.profile['REG_NICK'].replace('&rnd', rnd).replace('&ct', ct)

        ident = client.profile['REG_USER'].replace('&rnd', rnd).replace('&ct', ct)

        gecos = client.profile['REG_NAME'].replace('&rnd', rnd).replace('&ct', ct)


        # register

        if client.client_caps:
            client.sock_send(['CAP', 'LS', '302'])

        if client.profile['CON_PASS']:
            client.sock_send(['PASS', client.profile['CON_PASS']])

        client.sock_send(['NICK', nick])

        client.sock_send(['USER', ident, '0', '*', ':' + gecos])

