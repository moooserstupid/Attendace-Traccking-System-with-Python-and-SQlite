import qrcode

print("Enter QR code content:")
s = input()
img = qrcode.make(s)
img.save("QRCodes/" + s + ".png")
