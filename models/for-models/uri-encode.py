import urllib
import os, errno
from os import listdir
import PIL.Image as img

imageFiles = listdir("../output/ontario/304/")

del imageFiles[0]

print imageFiles[0]
print len(imageFiles)

image = [img.open("../output/ontario/304/%s"%fname) for fname in imageFiles]

img_height, img_width = image[0].size

maxWidth = (img_width * 6)
maxHeight = (img_height * 20)

sprite = img.new(
	mode='RGBA',
	size=(maxWidth, maxHeight),
	color=(0,0,0,0))

print "Sprite created..."

colCount = 0
rowCount = 0

for imgSprite in image:

	locx = img_width*colCount
	locy = img_height*rowCount

	print locx
	print locy

	sprite.paste(imgSprite,(locy,locx))

	if rowCount == 6:
		colCount += 1
		rowCount = 0

	rowCount += 1



		#print colCount

	#print loc

# 	for colCount 

# 	locationCol = img_width*colCount

# 	print locationCol

# # 	# location = img_width*count
# # 	# sprite.paste(imgSprite,(0,location))

# # 	#exit()

sprite.save('for-sprite.png')

print "Sprite saved"

exit()