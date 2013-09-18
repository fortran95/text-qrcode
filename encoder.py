# -*- coding: utf-8 -*-

class divider:

    _message = ''

    def __init__(self, message):
        self._message = message.encode('base64')
        self._message = self._message\
            .replace('+', '*')\
            .replace('/', '#')\
            .replace('\n', '')

    def divide(self, length):
        parts = []
        string = self._message
        i = 0

        while string != '':
            newpart = string[:length]
            string = string[length:]
            parts.append((newpart, i))
            i += 1

        ret = [self._pack(each[0], each[1], i-1) for each in parts]

        return ret

    def _pack(self, string, i, count):
        return ">m:%d>%s<m:%d<" % (i, string, count)

import random
src = ''.join(chr(random.randint(0,255)) for i in xrange(128))
x = divider(src)
print x.divide(64)
