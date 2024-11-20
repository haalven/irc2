
# process a raw server message

from strip_codes     import strip_codes
from msg_decode      import msg_decode
from msg_parser      import msg_parser
from source_parse    import source_parse
from time_calc       import dt_now, pre, st2dt
from blacklist       import blacklist
from message_key     import message_key
from ignore          import ignore
from display_fmt     import display_fmt
from xterm_control   import color, reset



def msg_process(client, line):

    decoded  = msg_decode(line)

    stripped = strip_codes(decoded)


    # parse msg and source

    msg = msg_parser(stripped)

    msg = source_parse(msg)


    # server-time

    msg['DATE'] = st2dt(msg['TAGS']['time']) if 'time' in msg['TAGS'] else dt_now()


    # check blacklist

    blacklist(client, msg)


    # add message key

    msg = message_key(client, msg)


    # ignore

    if ignore(client, msg): return None


    # write log

    client.write_log(msg['DATE'], stripped)


    # display

    if not (msg['VERB'] == 'PING' and client.hide_ping):

        if client.showraw:
            print(pre(msg['DATE']), color(109), line, reset())

        if client.showparsed:
            print(pre(msg['DATE']), color(108), msg, reset())

        display_fmt(client, msg)


    # interpreter

    client.msg_handle(msg)

