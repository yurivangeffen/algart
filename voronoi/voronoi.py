# https://rosettacode.org/wiki/Voronoi_diagram#Python
from PIL import Image
import random
import math
import os
import datetime
 
def generate_voronoi_diagram(width, height, num_cells):
	image = Image.new("RGB", (width, height))
	putpixel = image.putpixel
	imgx, imgy = image.size
	nx = []
	ny = []
	nr = []
	ng = []
	nb = []
	for i in range(num_cells):
		nx.append(random.randrange(imgx))
		ny.append(random.randrange(imgy))
		nr.append(random.randrange(128)+128)
		ng.append(random.randrange(128)+128)
		nb.append(random.randrange(128)+128)
	for y in range(imgy):
		if y%100 == 0:
			print(str(int(float(y)/float(imgy)*100)) + "%")
		for x in range(imgx):
			dmin = math.hypot(imgx-1, imgy-1)
			j = -1
			for i in range(num_cells):
				d = math.hypot(nx[i]-x, ny[i]-y)
				if d < dmin:
					dmin = d
					j = i
			if dmin < 10:
				putpixel((x, y), (nr[j]/2, ng[j]/2, nb[j]/2))
			else:
				putpixel((x, y), (nr[j], ng[j], nb[j]))

	name="VoronoiDiagram_"+datetime.datetime.now().isoformat()+".jpg"
	image.save(name, "JPEG")
	print("100%, " + name)
	image.show()

for x in xrange(1,2):
	generate_voronoi_diagram(3000, 4200, 25)
