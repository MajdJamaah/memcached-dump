"""
apt-get install python-memcache
apt-get install libmemcache-tools
"""
#!/usr/bin/python
import sys
import memcache
import subprocess
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
hostport = host+":"+port
s = memcache.Client([hostport])
print "checking keys..."
output = subprocess.check_output("memcdump --servers="+hostport, shell=True)
data= output.split('\n')
lista = {}
for key  in data:
    if key != '':
        try:
            lista[key]=s.get(key)
            print "dumping "+key+"..."
        except:
            print("An exception occurred")
jsonfinal = json.dumps(lista, ensure_ascii=False)
print "writing output..."
fileWrite = open(out, "w")
fileWrite.write(jsonfinal)
fileWrite.close()
print "memcache file created"
print "finish dump"
