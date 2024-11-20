

# handle user WHOAMI

from time_calc import dt_now, now, td2str
from socket import gethostbyaddr
from source_parse import source_expand
from networks import net_urls
from ircd_family import ircd_urls
from xterm_control import color, reset


def handle(client, kb_args):

    # data

    date   = now()

    verb   =  color(36) + '[WHOAMI]' + reset()

    net    = client.isupport['NETWORK'] if client.isupport['NETWORK'] else '[none]'
    neturl = str(net_urls(net))

    nick   = client.mynick if client.mynick else '[none]'

    ircd   = client.ircd_family if client.ircd_family else '[unknown]'
    ircdurl= str(ircd_urls(ircd))

    uptime = td2str(dt_now() - client.registered) if client.registered else '[not registered]'

    serv   = client.myserv if client.myserv else '[none]'

    try: servip = client.ircsock.getpeername()[0]
    except Exception: servip = '[none]'

    try: servhn = gethostbyaddr(servip)[0]
    except Exception: servhn = '[none]'

    sasl   = client.sasl_nick if client.sasl_nick else '[none]'

    oper   = client.opered

    services = []
    if client.profile['NICKSERV']:
        nsnick, _, __, ___ = source_expand(client.profile['NICKSERV'])
        services.append(nsnick)
    if client.profile['CHANSERV']:
        csnick, _, __, ___ = source_expand(client.profile['CHANSERV'])
        services.append(csnick)


    # output

    print(date, verb, 'profile :', client.profilename)
    print(date, verb, 'connect :', uptime)
    print(date, verb, 'network :', net, neturl)
    print(date, verb, 'ircd    :', ircd, ircdurl)
    print(date, verb, 'server  :', serv)
    print(date, verb, 'serverip:', servip, '('+servhn+')')
    print(date, verb, 'services:', services)
    print(date, verb, 'nickname:', nick)
    print(date, verb, 'account :', sasl)
    print(date, verb, 'operator:', oper)
    print(date, verb, 'channels:', client.mychans)
    print(date, verb, 'masters :', client.masters)

