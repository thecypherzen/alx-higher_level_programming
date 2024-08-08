#!/usr/bin/python3

import json
f = open("jsonfile.json", "w")
md = {1:3, 2:6, 3:9, 4:12}
l = json.dumps(md, indent=4)
json.dump(md, f, indent=4)
f.write(l)
s = json.loads(l)
print(l)
print(type(s))


#d = json.loads(l)
f.close()
#import os
#fwrite = open("./testfile.tx", "a+")
#fread = open("./testfile.tx", "r")
#content = fread.read()
#print(content)
#print("\n")
#for line in fread.read():
#    print(line)
#lines = ["another line \n", "another line\n", "another line\n"]
#fwrite.writelines(lines)
#fread.seek(0)
#content = fread.read()
#print(content)
#fwrite.truncate(0)
#fread.seek(0)
#fread.close()
#fwrite.close()
