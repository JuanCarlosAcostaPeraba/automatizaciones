#!/usr/bin/python3

import sys, pyqrcode, png

def qrcode(name, url):
    qr_code = pyqrcode.create(url);
    qr_code.png("/Users/juan/Downloads/" + name + ".png", scale = 5)

if __name__ == '__main__':
    try:
        qrcode(sys.argv[1], sys.argv[2])
        print("QR generated")
    except:
        pass