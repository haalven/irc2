
# nickname active ?

from casemapping import casemapped



def update_active(client, nick, dt):

    client.active_nicks[nick] = dt



def is_active(client, nick, dt):

    nick = casemapped(client, nick)

    for active in client.active_nicks:

        if casemapped(client, active) == nick:

            if (dt - client.active_nicks[active]) < client.active_delta:

                return client.active_nicks[active]

    return None
