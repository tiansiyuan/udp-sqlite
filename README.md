# udp-sqlite

[System config](mac-config.png).

First version uses process pool with python 3.6.1. It takes 3 hours to write into 8 Sqlite3 DBs, 3.2G for each size.

See [picture 1](fig-1.png) and [picture 2](fig-2.png).

Using pypy 5.8, the time would be reduced to half, 1.5 hours.

See [picture 3](pypy.png).

If harddisk partition is near full, the write speed becomes slow, but not for sure.
