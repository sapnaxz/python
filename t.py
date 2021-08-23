import pyqrcode

def qrcode():
    q = pyqrcode.create(input())
    q.png('tu.png', scale=6)
    print("yuppie QR code generated")

if __name__ == '__main__':
    qrcode()
    
