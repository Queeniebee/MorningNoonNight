import os, sys
import time
from datetime import date, datetime, time, timedelta

"""
if not os.access("/home/pi/www/mnn/", os.W_OK):
    print "No write access to proper directory"
    sys.exit(1)
"""

# display_file = open("/home/pi/www/mnn/index.html", "r")

display_file = open("index.html", "r")

display_file_lines = display_file.readlines()
display_file.close()

output_lines = []
lines_to_edit = ["<p class=\"script\">", "<h1 class=\"script\">"]
text = []

today = datetime.now()
t = str(today)

# for each line in our display file we need to check if it has the lines_to_edit tags
# text is what we want to write out to index.html regardless, so outside of if statement 
for line in display_file_lines:
    for tag in lines_to_edit:
    	if line.startswith(tag):
            line = tag + t + "</" + tag.split()[0][1:] + ">\n"
    text.append(line) 

display_file = open("index.html", "w")
# display_file = open("/home/pi/www/mnn/index.html", "w")

display_file_lines = display_file.write("".join(text))
display_file.close()

# get the date, time
# after adding three hours to the time variable, display a .png from a dictionary
# image is display from a browser
