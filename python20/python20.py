print("*** Converting hh.mm.ss to seconds ***")
h,m,s = map(int,input("Enter hh mm ss : ").split())

if h>=0 and m >= 0 and s >= 0 :
    second = int((h*3600)+(m*60)+s)
    if h >=10 :
        if m >= 10 and m < 60 and s >= 10 and s < 60:
            print("{}:".format(h)+"{}:".format(m)+"{} = {:,}".format(s,second),"seconds")
        elif m >=10 and m < 60 and s < 10:
            print("{}:".format(h)+"{}:0{}".format(m,s)+"= {:,}".format(second),"seconds")
        else :
            print("mm({})".format(m)+" is invalid!")
    elif h < 10 :
        if m < 10 and s < 10 :
            print("0{}:".format(h)+"0{}:".format(m)+"0{} = {:,}".format(s,second),"seconds")
        elif m < 10 and s >= 10 :
            print("0{}:".format(h)+"0{}:".format(m)+"{} = {:,}".format(s,second),"seconds")
        else :
            print("0{}:".format(h)+"{}:".format(m)+"{} = {:,}".format(s,second),"seconds")
    else :
        print("0{}:".format(h)+"0{}:".format(m)+"0{} = {:,}".format(s,second),"seconds")
else :
    if h < 0 :
        print("hh({})".format(h)+" is invalid!")
    elif m < 0 :
        print("mm({})".format(m)+" is invalid!")
    else :
        print("ss({})".format(s)+" is invalid!")