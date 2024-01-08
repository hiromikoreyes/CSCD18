### Polygon code
import numpy as np

#number of sides
n=5

#scale
r=80

polygon_pts = []
theta = []

#translate 
shift_x = 500
shift_y = 500

#rotate between [0, 2pi)
rotation =  2 * np.pi/6

for i in range(0, n):
    theta.append((i * 2 * np.pi) / n)

for angle in theta:
    polygon_pts.append((r * np.cos(angle + rotation) + shift_x, r * np.sin(angle + rotation) + shift_y))

### Drawing polygon with something
import sys
from PIL import Image, ImageDraw

#Create Image object
im = Image.new('RGB', (1000, 1000))
im.paste("white", (0,0, 1000, 1000))


#Draw line
for i in range(0, n-1):
    draw = ImageDraw.Draw(im)
    draw.line([polygon_pts[i], polygon_pts[i+1]], fill="red", width=10)
draw.line([polygon_pts[n-1], polygon_pts[0]], fill="red", width=10)



#Show image
im.show()