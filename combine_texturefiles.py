from PIL import Image 
from easygui import fileopenbox


"""
Repeats multiple pictures contained in folders onto a new image
This program is useful when editing certain game resources requiring multiple resolutions in one picture!


# Folders are required to contain the image at resolution of the folder name
# Images are required to have the same name as the original file
"""

original = fileopenbox().split("\\")[-1]
folders = ["64x64","32x32","16x16","8x8"]
file_original = Image.open(original)
combined = Image.new('RGBA', (file_original.size[0],file_original.size[1]))
x = 0
y = 0
for folder in folders:

	image = Image.open(folder+"\\"+original)
	#paste the image at location x, y:
	combined.paste(image, (x, y))
	x += image.size[0]

combined.save(original)
