#!/usr/bin/env python

import sys
from optparse import OptionParser
import Image
import ImageOps

#Parse
op = OptionParser()

op.add_option("-I", "--image", dest="_image",
                  help="Read an image")

(options, args) = op.parse_args()

if len(sys.argv) != 3:
    print op.print_help()
    sys.exit()

#Thumbnail
size =120,120
#Read image
im   = Image.open(options._image)
imgr = ImageOps.grayscale(im)
imgr.thumbnail(size, Image.ANTIALIAS)
imgr.save("temp","JPEG")
px = imgr.load()
f = open('out','w')

xsize, ysize = imgr.size

il = []

#hash
for i in range(1,ysize):
    l = []
    for j in range(1,xsize):
        l.append(chr(64 + (px[j,i] + (20 - px[j,i] % 20)) % 34))
    il.append(l)
for item in il:
    f.write("%s\n" % "".join(item))

for item in il:
    print "".join(item)

print xsize, ysize
