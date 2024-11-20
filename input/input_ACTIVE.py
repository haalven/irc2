

# handle user ACTIVE

from time_calc import dt_now, pre
from is_active import is_active


def handle(client, kb_args):

    if client.active_nicks:

        active_list = []

        date = dt_now()

        for nick in client.active_nicks:

            if is_active(client, nick, date):
                active_list.append(nick)

        print( pre(date) , '[ACTIVE]' , active_list )

