def minplatforms(arr,dep):
    arr.sort() #sort the arrival array
    dep.sort() #sort the departure array
    i=1        #pointing to the second index of arrival array
    j=0       #pointing to the first index of departure array
    c=1       #we need atleast 1 platform
    n=len(arr) 
    while(i<n):
        if(arr[i]>dep[j]): #if the arrival time is greater than departure time
            i+=1           #increment the start index of arrival array
            j+=1           #increment the start index of departure array
        else:              #else
            c+=1           #increment platform count
            i+=1           #increment the start index of arrival array

    return c

n=int(input("No of trains: "))
arr=[]
dep=[]

# Taking input for 'arr' and 'dep' arrays
print("Arrival time array: ")
for i in range(0, n):
    ele = int(input())
    # adding the element
    arr.append(ele) 

print("Departure time array: ")
for i in range(0, n):
    ele = int(input())
    # adding the element
    dep.append(ele) 

print(minplatforms(arr,dep))