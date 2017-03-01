#mshow numbers smaller than the gived by the user

llista = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []

user_given = input("give me a number... ")

for num in llista:

	if num < user_given:

		new_list.append(num)

print(new_list)
