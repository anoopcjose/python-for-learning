def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

nterms = 5

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Fibonacci sequence:")
   for i in range(nterms):
       print(recur_fibo(i))


# i = 5 , return(f(4) + f(3))
# i = 4 , return(f(3) + f(2))
# i = 3 , return(f(2) + f(1))
# i = 2 , return(f(1) + f(0))
# i = 1 , return 1
# i = 0 , return 0