
# loop: read the socket, user input

from cmd_input   import cmd_input
from round_robin import round_robin
from msg_process import msg_process


def sockread(client):

    if client.connected:

        read_buffer = b''


        # sockread loop
        while 1:

            data = b''

            # read socket (blocking)
            try: data = client.ircsock.recv(4096)

            # user input
            except KeyboardInterrupt:

                cmd_input(client)

                continue

            # read error
            except Exception as e:

                print('READ ERROR:', str(e))

                if not client.registered: # there was no 001 message
                    round_robin(client)

                client.connection_reset()

                return None


            # check

            if not data: return None # server died?

 
            # buffer voodoo
 
            data = read_buffer + data
            read_buffer = b''
            data_lines = [l.strip(b'\r') for l in data.split(b'\n')]
            if data_lines[-1]: read_buffer = data_lines[-1]
            data_lines.pop(-1)


            # process message(s)

            for line in data_lines: msg_process(client, line)

