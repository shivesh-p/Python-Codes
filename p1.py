def factorial(n):
	fact = 1
	for i in range(1,n+1):
		fact *= i
	return(fact)

if __name__ == "__main__":
	print("Enter the Integer :", end = " ")
	a = int(input())
	print("Factorial : ", factorial(a) )
