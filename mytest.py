import json
if __name__ == '__main__':
    res = []
    res.append(("qweqwe",12))
    res.append(("asdasda",2))
    res.append(("sadsad",3))
    res.append(("asdasdassadfgewfw",1))
    print (json.dumps(res))
    ok = json.dumps(res)
    print (ok)
    print (type(ok))
