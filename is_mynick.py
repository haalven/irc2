
# is my nick?

from casemapping import casemapped


def is_mynick(client, nick):


    nick = casemapped(client, nick)

    mynick = casemapped(client, client.mynick)


    if nick == mynick: return True

    elif nick == '*': return True

    else: return False

