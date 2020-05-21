def func2(m=10, n=5):
   sum1 = int(m) + int(n)
   return sum1

print(func2())  #prints 15

s1 = func2(100, 50)
print(s1)   #150

s1 = func2(100)
print(s1)   #105

s1 = func2(10, 5)
print(s1)   #15

s1 = func2()
print(s1)   #15