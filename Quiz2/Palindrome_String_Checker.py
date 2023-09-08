def palindrome(s):
    n=len(s)
    if(n==1):
        return "YES" #if string has only one character it is a palindrome
    i=0
    j=n-1
    while(i<j):
        if(s[i]==s[j]): #if the start character and last character are equal
            i+=1        #we increase the start by 1
            j-=1        #we decrease last character by 1
        else:
            return "NO" #if the two characters are not equal then it is not a palindrome
    return "YES"

s = input("Input the string: ")
print(palindrome(s))