#new list with just the repetitive numbers

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = []

for numa in a:

	if numa in b and numa not in new_list:

		new_list.append(numa)

print(new_list)
