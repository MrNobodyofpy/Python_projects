thang_30 = [4,6,9,11]
thang_31 = [1,3,5,7,8,10,12]
max_day = [30,31,28,29]

def leap_year(x):
    if x % 400 == 0 or (x % 4 == 0 and x % 100 != 0):
        return True
    else: return False
def so_hop_le(day,month,year):
    if month in range(1,13):
        if month in thang_30:
            if 1 <= day <= max_day[0]:
                return True
        elif month in thang_31:
            if 1 <= day <= max_day[1]:
                    return True
        else:
            if leap_year(year):
                if 1 <= day <= max_day[3]:
                    return True
            else:
                if 1<= day <= max_day[2]:
                    return True

while True:
    a,b,c,x,y,z = map(int,input().split())

    if so_hop_le(a,b,c) == True and so_hop_le(x,y,z) == True:
        break
if (c*10000 + b*100 + a) > (z*10000 + y*100 + x):
    print(2)
else: print(1)