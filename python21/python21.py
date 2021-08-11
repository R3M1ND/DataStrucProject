print(" *** Wind classification ***")
w = float(input("Enter wind speed (km/h) : "))

if w >= 0 and w <= 51.99 :
    print("Wind classification is Breeze.")
elif w >= 52.00 and w <= 55.99 :
    print("Wind classification is Depression.")
elif w >= 56.00 and w <= 101.99 :
    print("Wind classification is Tropical Storm.")
elif w >= 102.00 and w <= 208.99 :
    print("Wind classification is Typhoon.")
else :
    print("Wind classification is Super Typhoon.")
