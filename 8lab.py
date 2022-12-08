#1 - Factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = int(input("Санды енгізіңіз : "))
print("Факториал тең :  ",factorial(num))


#2 - Рекурсия
#Ryskeldi
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print()
tri_recursion(6)

#3-Көбейту кестесі
def newfunc(n,m):
    for i in range(1,11):# Бірінші көбейткіш
        for j in range(n,m+1):#Екінші көбейткіш
            print(f'\t{j} * {i} = {i * j}', end='') #Результат
        print('')
newfunc(1,9)

#Baken's function
def is_prime(num):
	if num &gt; 1:
	for i in range(2, num//2):
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
		else:
	print(num, "is a prime number")
	else:
	print(num, "is not a prime number")

