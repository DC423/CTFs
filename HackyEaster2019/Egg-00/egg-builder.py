import os
from PIL import Image

dir_path = os.path.dirname(os.path.realpath(__file__))
directory = os.fsencode(dir_path)
im_two = Image.new('RGB', (480,480), "black")
pixels = im_two.load()

i = 0
j = 0
for file in os.listdir(directory):
	filename = os.fsdecode(file)
	if filename.endswith(".png"):
		im_one = Image.open(filename, 'r')
		r,g,b = list(im_one.getdata())[0]
		print ("Setting pixel [" + str(i) + "," + str(j) + "] to (" + str(r) + "," + str(g) + "," + str(b) + ")\n") 
		pixels[i,j] = (r,g,b)
		i = i + 1
		if i%480 == 0:
			i = 0
			j = j+1
		im_one.close()
		continue
	else:
		continue

im_two.save("out-egg.png")