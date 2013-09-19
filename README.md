Converting between QRCode and Text
==================================

This is a tiny tool for 2 purposes:

1. Encrypt and divide a text into several qrcodes.
2. Join the scan result of all above qrcodes together and reconstruct the text.

The first job is done using a simple HTML page with Javascript, thanks to authors addressed in these libraries.

The QRCodes as results produced by this HTML page, can be easily published by making screensnaps.
This is useful for exchanging messages via such media, where plain text or even some letter combinations in Base64-encoded text will be **filtered** or worse, automatically **censored**.
So long as the media don't compress these QRCode images to a level that they are not readable, the message exchange is no problem.

Scanning QRCodes are not implemented, because there are very good scanners, e.g. ZBarImg, to do such jobs.
Using ZBarImg is here recommended, as this is the best QRCode Scanner I've ever seen, on Linux and Windows. It supports also scanning multiple QRCodes
in a same picture, which eases the job of users. The bulk information after the scanning can be directly pasted to this HTML page.
