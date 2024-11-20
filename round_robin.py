
# connect address -> fallback (round robin)

from time_calc import now


def round_robin(client):

    if client.profile['ROUNDROB']:

        if client.profile['CON_ADDR'] != client.profile['ROUNDROB']:

            print(now(), '*', 'using fallback address ...')

            client.profile['CON_ADDR'] = client.profile['ROUNDROB']

            return True

    return False

