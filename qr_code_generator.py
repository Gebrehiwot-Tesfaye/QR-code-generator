import qrcode

data=input ( 'Enter the text or URL to generate QR code: ' ).strip()   
filename=input ( 'Enter the filename to save the QR code (e.g., qr_code.png): ' ).strip()
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill_color="black", back_color="white")
img.save(filename)
print("QR code saved as",filename 
)