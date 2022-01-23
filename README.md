Cron Parser
=========
Description
-----------
This is a command line script which parses a cron string and expands each field
to show the times at which it will run.
It only considers the standard cron format with five time fields (minute, hour, day of month, month, and day of week) plus a command. <br>

The input will be on a single line.
The application accepts the cron string as a single argument, in the format 
`<minutes> <hour> <day_of_month> <<month> <day of week> <command>`. It will raise an error if it receives less or more than this.  <br>

The output will be formatted as a table with the field name taking the first 14 columns and the times as a space-separated list following it. <br>

Instructions
------------
In order to run this script locally, you should have python3 installed on your machine. <br>
From the root directory (the same that contains app.py), open your terminal and run: `python3 app.py <argument_string>`

Testing
-------
Unit tests are located in the tests directory. In order to run them, you will need to install the pytest module. Once that is done, simply run pytest.