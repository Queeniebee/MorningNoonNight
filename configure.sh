########################
#
# Initiate python script
#
########################

#!/bin/sh

#!/usr/bin/env python

sudo python scripts/time.py

# run a cron job here
1 2 3 4 5 USERNAME /path/to/command arg1 arg2

OR

1 2 3 4 5 USERNAME /path/to/script.sh


[minute, hours, day, month, day of week]

0 */3 * * * /path/to/script.sh >/dev/null 2>&1
