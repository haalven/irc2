

# display formatted messages

from copy import deepcopy
from time_calc import pre
from is_staff import is_staff
from is_bot import is_bot
from is_active import is_active
from is_mynick import is_mynick
from nick_color import nick_color
from match_format import links_fmt
from is_tag import is_tag
from xterm_control import *


def format(client, msg):

    # copy elements

    date   = pre( msg['DATE'] )

    source = deepcopy( msg['SRC']    )

    nick   = deepcopy( msg['NICK']   )

    target = deepcopy( msg['PAR'][0] )

    text   = deepcopy( msg['PAR'][1] )


    # now active?

    nowactive = not is_active(client, msg['NICK'], msg['DATE'])


    # target

    target_prefix = light() + '['+ target +']' + normal()  # default

    if is_mynick(client, target) or not client.registered:  # private msg

        target_prefix = color(136) + '[private]' + endcol()


    elif ('STATUSMSG' in client.isupport) and ('CHANTYPES' in client.isupport) \
    and len(target) > 1:

        if target[0] in client.isupport['STATUSMSG'] \
        and target[1] in client.isupport['CHANTYPES']:  # op msg

            target_prefix = light() + '['+ normal() + color(196) + target[0] \
                + endcol() + light() + target[1:] +']' + normal()



    # nick color

    nick = bold() + nick_color(source) + nick + endcol() + normal()


    # now active nick

    if nowactive: nick = uline() + nick + endul()


    # staff

    if is_staff(client, msg):
        nick = color(126) + '*' + nick

    # bot

    if is_bot(client, msg):
        nick += '\x20' + color(243) + 'BOT' + endcol()


    # member of blackset

    if msg['BLACK']: nick = chr(10071) + nick


    # action text

    if msg['KEY']=='ACTION':

        verb, _, text = msg['PAR'][1].strip('\x01').partition('\x20')


    # link format

    text = links_fmt(text, color(94), endcol())


    # bold mynick (you cannot re.compile(nick)!)

    i1 = text.lower().find(client.mynick.lower())
    if i1 != -1:
        i2 = i1 + len(client.mynick)
        text = text[:i1] + bold() + text[i1:i2] + normal() + text[i2:]


    # reply

    if is_tag(msg, '+reply') or is_tag(msg, '+react'):

        text = color(36) + '↳ ' + endcol() + text



    # construct and print

    line   = [ date , target_prefix , nick , text ]

    if msg['KEY'] == 'ACTION': line.insert(2,'\u261B')

    print( '\x20'.join(line) )

