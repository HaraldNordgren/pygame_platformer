#!/usr/bin/python

import requests
from PIL import Image
from StringIO import StringIO

import httplib
import shutil

#http://www.bghq.com/bgs.php?system=gen&game=s/s1&mode=green

base_directory = "/home/harald/pygame/2d-platformer/"

domain_url = "http://www.bghq.com/bgs/gen/s/s1/"
file_extension = ".png"

for i in range(0,110):
    number_string = str(i).zfill(3)
    image_url = domain_url + number_string + file_extension

    folder = base_directory + "images/green-hill-zone/"

    r = requests.get(image_url, stream=True)
    if (r.status_code == httplib.OK):
        print("  " + image_url)

        filename = folder + number_string + file_extension

        #with open(image_url, 'wb') as f:
        #    print "hej"
        #        r.raw.decode_content = True
        #        shutil.copyfileobj(r.raw, f)
        
        i = Image.open(StringIO(r.content))
        i.save(filename)
