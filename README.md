Cron Parser
=========

Description
-----------
This is a command line script which parses a cron string and expands each field
to show the times at which it will run.
I only consider the standard cron format with five time fields (minute, hour, day of
month, month, and day of week) plus a command.

 The input will be on a single line.
The cron string will be passed to your application as a single argument.
~$ your-program "*/15 0 1,15 * 1-5 /usr/bin/find"


Instructions
------------
From the application root, run  `<python3 parse.py "*/15 0 1,15 * 1-5 /usr/bin/find"`
The answer should be similar to below: <br>

minute 0 15 30 45
hour 0
day of month 1 15
month 1 2 3 4 5 6 7 8 9 10 11 12
day of week 1 2 3 4 5
command /usr/bin/find

Caveats
-------


