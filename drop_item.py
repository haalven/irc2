
# drop an item from iterable
# e. g. remove #channel from mychans
# e. g. remove nick from active_nicks


from casemapping import casemapped


def drop_item(client, iter, key):

    key = casemapped(client, key)

    for item in iter:

        if casemapped(client, item) == key:

            if type(iter) == list:

                while item in iter: iter.remove(item)

                return

            elif type(iter) == dict:

                del iter[item]

                return

