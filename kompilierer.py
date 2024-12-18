import os
import img2pdf

directory_png = "bilder/png"


img_dirs = []

for filename in os.listdir(directory_png):
    full_path = os.path.join(directory_png, filename)
    img_dirs.append(full_path)


for img in img_dirs:
    file = os.path.basename(img)[:-4]
    with open(f'bilder/pdf/{file}.pdf', 'wb') as f:
        f.write(img2pdf.convert(img))
