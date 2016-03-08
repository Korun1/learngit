import json
def run_year(year):
    year = int(year[0:4])
    #print (year)
    if year%4==0 and year%100!=0:
        return 1
    if year%400==0:
        return 1
    return 0

def before_day(year,n):
    Y = int(year[0:4])
    M = int(year[4:6])
    D = int(year[6:])
    if D > n:
        string = str(D-n)
        return year[0:6] + string if (D-n) >= 10 else year[0:6] + "0" + string
    else:
        if M == 1:
            last = n - D
            return str(Y-1) + "12" + str(31-last)
        elif M == 3:
            last = n - D
            if run_year(year) == 1:
                string = str(29 - last)
                return year[0:4] + "02" + string
            else:
                string = str(28 - last)
                return year[0:4] + "02" + string
        elif M == 2 or M == 4 or M == 6 or M == 9 or M == 11:
            last = n - D
            string = str(31 - last)
            return year[0:4] + str(M-1) + string if (M-1) >= 10 else year[0:4] + "0" + str(M-1) + string
        else:
            last = n - D
            string = str(30 - last)
            return year[0:4] + str(M-1) + string if (M-1) >= 10 else year[0:4] + "0" + str(M-1) + string
           
if __name__ == '__main__':
    ok = input()
    n = input()
    n = int(n)
    while(ok!="end"):
        print(before_day(ok,n))
        ok = input()
        n = int(input())
