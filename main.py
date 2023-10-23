import qrcode
img = qrcode.make('https://forms.gle/pZoeLruHy97tx4Ej7')
type(img)  # qrcode.image.pil.PilImage
img.save("link.png")