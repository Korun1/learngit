count = {}
res = input()
while res != "end":
    if res not in count:
        count[res] = 0
    count[res] += 1
    res = input()
ans = sorted(count.items(),key=lambda o:o[1],reverse = True)
for i in ans:
    print (i[0],i[1])
