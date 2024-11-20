
# user command input

from xterm_control import color, endcol, clear


def cmd_input(client):

    try:

        # keyboard input

        kb_in = input(clear() + color(36) + '> ' + endcol())

        # execute

        client.user_cmd(kb_in.strip())


    except KeyboardInterrupt:

        # return to sockread

        print(clear(), end='')


    except Exception as e:

        print('INPUT ERROR:', str(e))

        client.connection_reset()

        return None
