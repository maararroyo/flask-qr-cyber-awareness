import qrcode

url = " https://c4c9-189-147-248-190.ngrok-free.app"  
img = qrcode.make(url)
img.save("codigo_qr.png")
