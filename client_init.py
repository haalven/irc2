
# initialize the "client" object

from socket         import socket
from os             import system, environ
from time           import time
from datetime       import timedelta
from time_calc      import now
from getpass        import getpass
from chan_privs     import chan_privs
from client_caps    import client_caps
from tabcomplete    import init_readline
from load_profile   import load_profile
from casemapping    import load_casemaps


def client_init(client, profile_name):

    '''
    GENERAL CLIENT SETTINGS
    '''

    # local irc path

    try: client.ircpath = environ['irc']
    except Exception: exit('Error: "$irc" missing')


    # show raw messages

    client.showraw = False


    # chan-privs

    client.chan_privs = chan_privs()


    # my caps

    client.client_caps = client_caps(client)


    # hide ping?

    client.hide_ping = True


    # hide outgoing messages?

    client.hide_send = False


    # remote bot enabled?

    client.remotebot = True


    # time diff for active nicks

    client.active_delta = timedelta(minutes=10)


    # create the socket object

    client.ircsock = socket()


    # load casemaps

    load_casemaps(client)
    client.casemap = ''


    # initialize readline/tabcompleter

    init_readline(client)



    '''
    PROFILE RELATED SETTINGS
    '''

    # the profile name
 
    client.profilename = profile_name


    # set tmux title

    tmuxname = profile_name.replace('bnc_', '').replace('#', '')

    system(f'tmux rename-window {tmuxname} 2> /dev/null')


    # load profile json

    client.profile = load_profile(client.ircpath, profile_name)

    print(now(), '*', f'profile "{profile_name}" loaded .')


    # security check

    if client.profile['SASL_PWD'] and not client.profile['CON_ENCR']:
        exit('Error: encrypt to send password')


    # ask for sasl password

    while client.profile['SASL_PWD'] == '&enter':
        client.profile['SASL_PWD'] = getpass('SASL password:')


    # reconnect timer

    client.reconnect = client.profile['CON_RECO']

    # touch the logfile

    client.logfile = client.ircpath + '/slogs/' + str(time()) + \
        '-' + profile_name + '-socket.log'

    open(client.logfile, 'w', encoding='utf-8').close()


    # show traffic ?

    client.hide_traffic = not client.profile['SHOWTRAF']
