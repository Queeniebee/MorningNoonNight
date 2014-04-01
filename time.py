import os, sys
import time
from datetime import date, datetime, time, timedelta


if not os.access("/home/pi/www/mnn/", os.W_OK):
    print "No write access to proper directory"
    sys.exit(1)

display_file = open("/home/pi/www/mnn/index.html", "r")

display_file_lines = display_file.readlines()
display_file.close()
output_lines = []

lines_to_edit = ["<p class=\"script\">", "<h1 class=\"script\">"]

duration = timedelta(hours=3)

today = datetime.date.today()

for line in display_file



text += display_text 
display_file = open("/home/pi/www/mnn/index.html", "w")
display_file_lines = display_file.write(text)
display_file.close()

# get the date, time
# after adding three hours to the time variable, display a .png from a dictionary
# image is display from a browser
