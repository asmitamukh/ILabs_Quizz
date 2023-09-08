def atm(X,Y):
    if(X%5==0 and Y>=X+0.50): #check if amount to be withdrawn is a multiple of 5 and available balance is greater than amount to be withdrawn plus trabsaction charge
        Y=Y-X-0.5            #update the available balance if it meets the condition


    return(Y)

a=int(input("Amount Of Cash To Be Withdrawn: "))
b=float(input("Pooja's initial account balance: "))
print("Current balance is: ",atm(a,b))
