def computing_lcm():

   x = int(input("Enter a number       : "))
   y = int(input("Enter another number :"))
   if x > y:
       bigger = x
   else:
       bigger = y

   while(True):
       if((bigger % x == 0) and (bigger % y == 0)):
           lcm = bigger
           break
       bigger += 1

   return lcm

print("The L.C.M. is", computing_lcm())
