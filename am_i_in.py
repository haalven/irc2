
# am i a member of #channel ?

from casemapping import casemapped
from is_channel import is_channel
from time_calc import now


def am_i_in(client, channel):


    # check argument

    if type(channel) != str: return False

    if not channel: return False


    # a valid channel?

    if not is_channel(client, channel):

        return False


    # in mychans?

    chan_casemapped = casemapped(client, channel)

    for mychan in client.mychans:

        if casemapped(client, mychan) == chan_casemapped:

            return True

    # not found

    print(now(), chr(9888) + chr(65039), ' you are not a member of:', channel)

    return False
