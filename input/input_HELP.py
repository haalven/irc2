

# handle user (?)HELP

from json import load
from time_calc import now


def handle(client, kb_args):


    helpfile = client.ircpath + '/help.json'

    with open(helpfile) as f: commands = load(f)

    if not kb_args[0]:

        print(now(), commands.keys())


    else:

        topic = kb_args[0].upper()

        if topic in commands:

            print(now(), 'descr:', commands[topic][1])
            print(now(), 'usage:', commands[topic][0])

        else:

            print(now(), topic, 'is not implemented .')

