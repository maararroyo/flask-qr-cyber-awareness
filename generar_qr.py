import qrcode

url = "https://flask-qr-cyber-awareness.onrender.com"  
img = qrcode.make(url)
img.save("codigo_qr.png")
