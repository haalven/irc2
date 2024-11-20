

# handle 366 (RPL_ENDOFNAMES)

from copy import deepcopy
from time_calc import pre
from namesave import namesave
from is_staff import src_is_staff
from xterm_control import light, color, reset


def handle(client, msg):

    date  = pre(msg['DATE'])
    chan  = deepcopy(msg['PAR'][1])


    if chan in client.names_dict:

        # member dictionary (local copy)
        mdict = deepcopy(client.names_dict[chan])
        client.names_dict.pop(chan)


        # save mdict to /members
        namesave(client, chan, mdict)


        # ops and opers
        privslist = []

        '''
        def in_opers(addr, operhosts):
            for pattern in operhosts:
                if pattern.lower() in addr.lower():
                    return True
            return False
        '''

        for status in mdict:
            if status in ['user','voice']: continue
            for member in sorted(mdict[status], key=str.lower):
                # rpartition() splits at the last occurence of '!'
                if member.startswith('!'): nick, _, addr = member.rpartition('!')
                else: nick, _, addr = member.partition('!')
                if nick:
                    if src_is_staff(client, nick[1:] + '!' + addr):
                        nick = '*' + nick
                    privslist.append(nick)


        # member_info
        chan_members = []

        total = 0

        for status in mdict:
            count = len(mdict[status])
            total += count

            if count:
                statustxt  = str(count) + '\x20' + status
                statustxt += 's' if count>1 else ''

                chan_members.append(statustxt)

        member_info = ', '.join(chan_members)

        if len(chan_members) > 1:
            member_info += ' (total: ' + str(total) + ')'


        # formatting

        privs = light() + '\x20'.join(privslist) + reset()

        for prefix in list(client.chan_privs):
            privs = privs.replace(prefix,
                reset() + color(53) + prefix + reset() + light())
        privs = privs.replace('*',
                reset() + color(126) + '*' + reset() + light())


        # output

        print(date, chan, 'members:', member_info)

        if privslist:
            print(date, chan, 'ops:', privs)

