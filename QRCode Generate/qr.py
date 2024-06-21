import qrcode
from PIL import Image

# Create a QRCode object with specific parameters
qr = qrcode.QRCode(
    version=1,  # controls the size of the QR Code (1 is the smallest)
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
    box_size=5,  # size of each box in the QR code grid
    border=1  # thickness of the border
)

# Add data to the QR code
data = "https://github.com/Bhojrajsingh2000/Python-Project"
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill_color="black", back_color="white")

# Save the generated QR code as an image file
img.save("Python-Project-github-repository.png")
