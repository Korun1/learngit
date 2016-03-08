# -*- coding:utf-8 -*-
import json


res = {}
ok = input()

while ok != "end":
    nn = (ok,"reddddd")
    if nn not in res:
       res[nn] = 1 
    else:
        res[nn] += 1
    ok = input()

sorted_res = sorted(res.items(),key=lambda o:o[1],reverse = True)

print (sorted_res)
for key in sorted_res:
    #print (type(key))
    #print ("%s %d"%(key[0],key[1]))
    print (json.dumps(key))
    print (json.loads( json.dumps(key) ))
