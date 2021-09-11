def hbd(year):
    if year %2 == 0:
        base = int(year/2)
        print("saimai is just 20, in base {}!".format(base))
    else :
        base = int(year/2)
        print("saimai is just 21, in base {:2}!".format(base))
    

year = int(input("Enter year : "))
hbd(year)