import qrcode
from PIL import Image
import os

def generate_QR(data, output_file, logo_path=None):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
    
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill='black', back_color='white')
    
    if logo_path:
        logo = Image.open(logo_path)
        pos = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
        img.paste(logo, pos)
    
    print(f"Saving image to: {output_file}")
    img.save(output_file)
    
    if not os.path.exists(output_file):
        print(f"Error: File not found at {output_file}")
    else:
        print(f"Image saved successfully to {output_file}")

choice = input("Enter '1' for URL or '2' for image file: ")

if choice == '1':
    url = input("Enter the URL: ")
    generate_QR(url, "F:\\QR CODE\\QR_OUT.png")
elif choice == '2':
    image_path = input("Enter the path to the image file: ")
    generate_QR(image_path, "F:\\QR CODE\\image_QR_OUT.png", logo_path=image_path)
else:
    print("Invalid choice. Please enter '1' for URL or '2' for image file.")




    
    
                            
                       
                       