#mostrar todos los possibles divisores del numero dado por el usuario

user_number = int(raw_input("Numero...?"))

possible_divisors = range(1,user_number)

divisor_list = []

for n in possible_divisors:

	if user_number % n == 0:

		divisor_list.append(n)

print(divisor_list)