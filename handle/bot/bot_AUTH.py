

# handle bot_AUTH

MYHASH = '----sha3_256_hash----'


from hashlib import sha3_256
from time_calc import now


def handle(client,msg,bot_arg):

    if not bot_arg: return None

    print(now() ,'*','password check ...')

    passwd = bytes(bot_arg,'utf-8')
    digest = sha3_256(passwd).hexdigest()

    if digest == MYHASH:

        if not msg['SRC'] in client.masters: client.masters.append(msg['SRC'])

        client.sock_send( ['NOTICE', msg['NICK'], 'OK.'] )

    else: print(now() ,'*','... has failed.')
