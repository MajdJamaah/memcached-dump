"""
apt-get install python-memcache
apt-get install libmemcache-tools
"""
#!/usr/bin/python
import sys
import memcache
import json

out = "memdump"
host = "127.0.0.1"
port = "11211"

if "-f" in sys.argv:
        out = sys.argv[sys.argv.index("-f")+1]
if "-h" in sys.argv:
        host = sys.argv[sys.argv.index("-h")+1]
if "-p" in sys.argv:
        port = sys.argv[sys.argv.index("-p")+1]
print "conecting..."
s = memcache.Client([host+":"+port])
print "reading dumpfile..."
c = open(out, 'r').read()
try:
    decoded = json.loads(c)
    for key in decoded:
        try:
            s.set(str(key),str(decoded[key]))
            print "inserting  "+key+"..."
        except:
            print "something went wrong"
except (ValueError, KeyError, TypeError):
    print "JSON format error"
print "restore finished"
