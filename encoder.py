# -*- coding: utf-8 -*-

class divider:

    _message = ''

    def __init__(self, message):
        self._message = message.encode('base64')
        self._message = self._message\
            .replace('+', '*')\
            .replace('/', '_')\
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
        return ")m:%d)%s(m:%d(" % (i, string, count)

def get_html(divisions):
    urls = ["https://chart.googleapis.com/chart?chs=250x250&cht=qr&chl=%s" % i for i in divisions]
    return ''.join(['<img src="%s"></img>' % i for i in urls])

src = """
-----BEGIN PGP MESSAGE-----
Version: GnuPG v2.0.21 (MingW32)

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
hUOoNKRXWyKCGg==
=BVat
-----END PGP MESSAGE-----
"""

x = divider(src)
divided = x.divide(512)
print get_html(divided)
