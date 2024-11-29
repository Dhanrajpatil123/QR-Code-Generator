# pip install pyqrcode
# pip install pypng

import pyqrcode as p

content = "This is my content"

url = p.create(content)

url.png("myqr.png", scale = 5)

print("QR Code Generated Successfully...")