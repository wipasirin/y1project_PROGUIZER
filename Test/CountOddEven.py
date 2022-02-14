# count odd and even in 1 to number that user input
n = int(input("Please enter a number : "))

if (n>=1 and n<=99):
    if (n%2==0): # if n == even: the mount of 1 to n: even == odd = n/2
        even = int(n/2)
        odd = int(n/2)
        print("even =",even,"odd =",odd)
    else: # if n == odd: the mount of 1 to n: even+1 == odd = (n+1)/2
        even = int((n-1)/2)
        odd = int((n+1)/2)
        print("even =",even,"odd =",odd)

else:
    print("out of length")
