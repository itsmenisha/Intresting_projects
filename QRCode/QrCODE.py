# code .
import qrcode
img = qrcode.make('https://www.nishagnawaly.com.np/')
img.save("qr_scanner.png")
