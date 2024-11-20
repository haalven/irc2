

# handle user SYS

from os import system

def handle(client, kb_args):

    if not kb_args[0]: return None

    system( '\x20'.join(kb_args) )

