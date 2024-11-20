
# tab completer (readline)

import readline

'''
macOS: ~/.editrc
  python:bind -v
  python:bind ^I rl_complete
'''

from is_active import is_active
from time_calc import dt_now


def init_readline(client):


    def tabcomplete(client, begin, state):

        begin = begin.lower()

        results = []


        # active nicknames

        for anick in client.active_nicks:  # anick is lower()

            if is_active(client, anick, dt_now()):

                if anick.startswith(begin) and anick != begin:

                    results.append(anick)


        # my nickname

        if not client.mynick in results:

            if client.mynick.lower().startswith(begin) and client.mynick.lower() != begin:

                results.append(client.mynick)


        # my chans

        for chan in client.mychans:

            if chan.lower().startswith(begin) and chan.lower() != begin:

                results.append(chan)


        results.append(None)

        return results[state]



    def _tabcomplete(begin, state):

        return tabcomplete(client, begin, state)



    readline.parse_and_bind('tab: complete')

    readline.set_completer_delims('\x20')

    readline.set_completer(_tabcomplete)

