#!/bin/bash

gcc db1.c -o db1 -l sqlite3 
gcc db2.c -o db2 -l sqlite3
gcc db3.c -o db3 -l sqlite3
gcc db4.c -o db4 -l sqlite3
gcc db5.c -o db5 -l sqlite3
gcc db6.c -o db6 -l sqlite3
gcc db7.c -o db7 -l sqlite3
gcc app_db.c -o app_db -l sqlite3