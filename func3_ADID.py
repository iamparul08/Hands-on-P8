def func3(m, n=5):
   sum1 = int(m) + int(n)
   return sum1

s1 = func3(30, 20)
print(s1)   #50

s1 = func3(30)
print(s1)   #35

s1 = func3(5, 0)
print(s1)   #5

s1 = func3(8)
print(s1)   #missing one positional argument 'm' if there is no parameter