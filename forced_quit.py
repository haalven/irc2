
# forced quit?


def forced_quit(quitmsg):

    quitmsg = quitmsg.lower()

    if (quitmsg.startswith('kill') \
        and not (('nickserv' in quitmsg) \
        or ('nickname regained' in quitmsg) \
        or ('ghost command used' in quitmsg))) \
        or quitmsg.startswith('k-line') \
        or quitmsg.startswith('z-line') \
        or quitmsg.startswith('g-line') \
        or quitmsg.startswith('autokilled') \
        or quitmsg.startswith('operserv') \
        or quitmsg.startswith('banned'):
        #or quitmsg.startswith('excess flood'):
        #or quitmsg.startswith('max sendq'):

        return True

    else: return False
