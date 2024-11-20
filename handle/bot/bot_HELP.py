

# handle bot_HELP


def handle(client,msg,bot_arg):

    if msg['SRC'] in client.masters:

        commands = {
            'AUTH':     '!AUTH <password>',
            'ASCII':    '!ASCII <target> <file>',
            'BAN':      '!BAN <channel> <mask>',
            'CYCLE':    '!CYCLE <channel>',
            'DEAUTH':   '!DEAUTH [source]',
            'DO':       '!DO <ircd command>',
            'HELP':     '!HELP [CMD]',
            'IN':       '!IN',
            'PARTALL':  '!PARTALL',
            'SAY':      '!SAY <target> <text>',
            'STATUS':   '!STATUS',
            'STOP':     '!STOP',
            'TIME':     '!TIME'
        }

        try:
            client.sock_send( ['NOTICE', msg['NICK'],
                ':usage:', str(commands[bot_arg.upper()])] )

        except Exception:
            client.sock_send( ['NOTICE', msg['NICK'],
                ':'+str(commands.keys())] )
