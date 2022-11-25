
i = "HELLO USER! - This is a text based user interface where we calculate (leap/non-leap) year between two give year(dd/mm/yyyy)"
d = ("START CALCULATION--(YES/NO)")
print(d)
e = ("INFO--(ABOUT)")
print(e)
g = ("QUIT CALCULATION--(quit)")
print(g)
print(" ")
h = input()
if h.upper().lower().strip()=="yes":
    print("Congrats!")
    print(" ")
    print("Now We Are On First Level")
    print("ENTER YOU STARTING DATE - FORMATE (DD/MM/YYYY)-----ONE BY ONE------")
    


    date1 = int(input("ENTER STARTING DATE - ", ))
    if date1>31:
        print("ENTER VALID DATE")



    month1 = int(input("ENTER STARTING MONTH - ", ))
    if month1>12:
        print("ENTER VALID DATE")


    s_year = int(input("ENTER STARTING YEAR - ", ))
    print("  ")
    print("YOU STARTING DATE IS -", date1,"/",month1,"/",s_year)
    print("CONGRATS! - NOW WE ARE ABOUT TO COMPLETE THE PROCESS")
    print(" ")
    print("ENTER YOU ENDING DATE - FORMATE (DD/MM/YYYY)---ONE BY ONE----")

    date2 = int(input("ENTER YOU ENDING DATE - "))  
    if date2>31:
        print("ENTER VALID DATE")



    month2 = int(input("ENTER YOU ENDING MONTH - "))
    if month2>12:
        print("ENTER VALID DATE")
    e_year = int(input("ENTER YOU ENDING YEAR - "))
    print("  ")
    print("YOU ENDING DATE IS -", date2,"/",month2,"/",e_year)
    print(" ")
    for year in range(s_year,e_year+1):
        if year%100==0 or (year%4==0 and year%100 !=0):
            print(year,end=" ")
    print("<--This is your required leap year")
    print("")

    for year in range(s_year,e_year+1):
        if year%100 == 0 or (year%4 !=0 and year%100!=0):
            print(year,end=" ")
    print(",--this is not leap year")
else:
    if h.upper().lower().strip()=="about":
        print(i)
    else:
        if h.upper().lower().strip()=="quit":
            print("YOU LOST - BETTER LUCK NEXT TIME")
        else:
            if h.upper().lower().strip()=="no":
                print(" TRY IT ONCE")
        




    
