# # pip install pyzbar
# #  pip install pillow 

# from pyzbar.pyzbar import decode

# from PIL import Image

# # reading image
# img = Image.open("myqr.png")

# content = decode(img)

# print(content[0].data.decode())

import os
from pyzbar.pyzbar import decode
from PIL import Image

# Add the directory containing libzbar.dll 

# Read the QR code
img = Image.open("myqr.png")
content = decode(img)
print(content[0].data.decode())
