# Quantcast Log Processor - Most Active Cookie
## Usage
usage: 3700ftp.py -d specified-date [-h]

required arguments:

**-d specified-date**  
specifies the date at which the most active cookie should be found from.

optional arguments:

**-h, --help**  
show this help message and exit

-----

## Functionality
This program processes the log file and returns the most active cookie for specified day, given a cookie log file. The most active cookie as one seen in the log the most times during a given day. If multiple cookies meet that criteria, all of them are returned.

Each cookie in the cookie log file is in the following format: cookie,timestamp

Example:

AtY0laUfhglK3lC7,2018-12-09T14:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-09T10:13:00+00:00
5UAVanZf6UtGyKVS,2018-12-09T07:25:00+00:00
AtY0laUfhglK3lC7,2018-12-09T06:19:00+00:00
SAZuXPGUrfbcn5UA,2018-12-08T22:03:00+00:00
4sMM2LxV07bPJzwf,2018-12-08T21:30:00+00:00
fbcn5UAVanZf6UtG,2018-12-08T09:30:00+00:00
4sMM2LxV07bPJzwf,2018-12-07T23:30:00+00:00

for the specified date 2018-12-08 would return  
SAZuXPGUrfbcn5UA  
4sMM2LxV07bPJzwf   
fbcn5UAVanZf6UtG
