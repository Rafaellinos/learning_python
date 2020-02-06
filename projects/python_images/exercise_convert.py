from PIL import Image, ImageFilter
import sys
import os

print("""
Please inform the folder where contains the images to convert
and the folder to send the converted images. If the folder to
send does not exist, it will be created.
""")
try:
    folder_in = sys.argv[1]
    folder_out = sys.argv[2]
except Exception as err:
    print("Erro: missing parameter")
    exit()

if not os.path.exists(folder_in):
    print(f"The folder {folder_in} does not exist!")
    exit()
if not os.path.exists(folder_out):
    print(f"The output folder does not exist, creating one...")
    os.makedirs(folder_out)

if  not(folder_in.endswith('/')):
    folder_in = folder_in+'/'
if not(folder_out.endswith('/')):
    folder_out = folder_out+'/'

only_imgs = [x for x in os.listdir(folder_in) if '.jpg' in x]
print(f"Images that will be converted into pngs: \n"+' '.join(only_imgs))


for img in only_imgs:
    print(f'Converting {img}...')
    opened_img = Image.open(folder_in+img)
    opened_img.save(folder_out+"new_"+img.replace('jpg','png'))

