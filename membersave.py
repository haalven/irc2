
# save data collected by /MEMBERS

from copy import deepcopy
from is_staff import src_is_staff
from blacklist import isblack
from os import system
from time_calc import now


def membersave(client):

    # channel name; reset
    channel = client.member_save; client.member_save = False

    # copy dict
    unsorted_members = deepcopy(client.who_dict); client.who_dict = {}
    if not len(unsorted_members): return None

    # sort A-Z by nickname
    membernicks, members = sorted(unsorted_members.keys(), key=str.lower), {}
    for nick in membernicks: members[nick] = unsorted_members[nick]

    # new list of lines
    memberlines = []

    for nick in members:
        username, host, realname, server, flags = members[nick]
        address = username + '@' + host
        realname = realname.replace(chr(34), chr(8221)) # fake double quotes

        # channel priv
        priv = ''
        for p in client.chan_privs:
            if p in flags: priv = p; break

        # oper
        oper = ''
        if '*' in flags: oper = '*'
        elif src_is_staff(client, nick + '!' + address): oper = '+'

        # blacklist
        black = '!' if isblack(client, nick + '!' + address) else ''

        # construct and append line
        line = [priv, oper, black, nick, address, server, '"'+realname+'"']
        memberlines.append(line)


    # privs sort
    sortedlines = []
    for p in client.chan_privs:
        for l in memberlines:
            if l[0] == p: sortedlines.append(l)
    for l in memberlines:
        if not l[0]: sortedlines.append(l)

    # join comma-separated
    csvlines = []
    for line in sortedlines: csvlines.append(','.join(line))

    # header
    csvlines.insert(0, 'Priv,Oper,Black,Nickname,Address,Server,Realname')

    # construct filename
    def safename(s):
        s, safe = s.lower().replace('#', ''), ''
        for c in s: safe += c if (c in 'abcdefghijklmnopqrstuvwxyz012345679-') else '_'
        return safe if safe else '_'
    memberfile  = client.ircpath + '/members/members-'
    memberfile += safename(client.isupport['NETWORK']) + '.'
    memberfile += safename(channel) + '.csv'

    # write csv file
    with open(memberfile, 'w') as f: f.write('\n'.join(csvlines) + '\n')

    print( now() , '[MEMBERS]' , 'saved to' , memberfile )

    # open csv file with tabview
    # (pip install tabview)
    #system(f'tabview -w max "{memberfile}" 2> /dev/null')

