try:
    ok = open("test.txt",'r')
    for line in ok:
        print (line)
except IOError:
    print ("catch error")
try:
    print (aa)
except NameError,msg:
    print (msg)
