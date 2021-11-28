import qrcode

code = qrcode.QRCode(version=1, error_correction= qrcode.constants.ERROR_CORRECT_L, box_size=100, border=2)

code.add_data("https://github.com/Alperencode") # url here
code.make(fit=True)

image = code.make_image(fill_color="black", back_color="white")
image.save("QRCode.png")