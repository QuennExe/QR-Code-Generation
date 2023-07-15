# QR Code Generation
# Do the necessary downloads by typing "pip install qr pillow"  and " pip install qrcode" into the terminal
# @Lolita
import qrcode


code = qrcode.make('https://github.com/QuennExe') # Paste the link where you want to generate the QR code
code.save('vol1.png')

# OR

code = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
   box_size=  50,
    border = 2
)
code.add_data('https://github.com/QuennExe')
code.make(fit=True)
image= code.make_image(fill_color="Pink" , back_color="Black")
image.save('vol2.png')



