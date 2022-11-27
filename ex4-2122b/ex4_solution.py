''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def least_popular_characters(my_string):

	counter_chars = {}
	for char in my_string:
		if counter_chars.get(char) == None:
			counter_chars[char] = 0
		else:
			counter_chars[char] += 1

	min_counter = min(counter_chars.values())
	return_lst = []
	for char, counter in counter_chars.items():
		if counter == min_counter:
			return_lst.append(char)
	return " ".join(sorted(return_lst))

#########################################
# Question 2 - do not delete this comment
#########################################
def mult_sparse_matrices(lst):

	if len(lst) > 0:
		final_matrice = lst[0].copy()
		for coor in final_matrice.keys():
			final_result = final_matrice[coor]
			for matrice in lst[1:]:
				if matrice.get(coor, -1) != -1:
					final_result *= matrice.get(coor)
				else:
					final_result = 0
			final_matrice[coor] = final_result
		new_dict = {}
		for coor in final_matrice.keys():
			if final_matrice[coor] != 0:
				new_dict[coor] = final_matrice[coor]
		return new_dict
	else:
		return {}

#########################################
# Question 3 - do not delete this comment
#########################################
def fill_substring_dict(s, d, k):

	copy_dict = d.copy()
	for key in copy_dict.keys():
		if len(key) <= k:
			i = 0
			while i < len(s):
				index = s.find(key, i)
				if index != -1:
					copy_dict[key].append(index)
					i = index
				i += 1
	return copy_dict


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):

	new_dict = {}
	for tuple in tuples_lst:
		if tuple[0].lower() in new_dict.keys():
			new_dict[tuple[0].lower()].append(tuple[1].lower())
		else:
			new_dict[tuple[0].lower()] = [tuple[1].lower()]
	return new_dict

def num_courses_per_student(stud_dict):

	for key in stud_dict.keys():
		stud_dict[key] = len(stud_dict[key])

#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################

if __name__ == '__main__': #Do not delete this line!
	# Q1
	print(least_popular_characters('aabbAA') == 'A a b')

	# Q2
	print(mult_sparse_matrices([{(1, 3): 2, (2, 7): 1}, {(1, 3): 6}]) == {(1, 3): 12})
		
	# Q3
	print(fill_substring_dict('TTAATTAGGCGCTA', {'TA': [], 'G': [], 'K': [], 'TTAA': [], 'tat': [], 'TTA': []}, 3) == {'TA': [1, 5, 12], 'G': [7, 8, 10], 'K': [], 'TTAA': [], 'tat': [], 'TTA': [0, 4]} )

	# Q4
	stud_dict = courses_per_student([('Tom', 'Math'), ('Oxana', 'Chemistry'), ('Scoobydoo', 'python'), ('Tom', 'pYthon'), ('Oxana', 'biology')])
		
	print(stud_dict == {'tom': ['math', 'python'], 'oxana': ['chemistry', 'biology'], 'scoobydoo': ['python']})
		
	num_courses_per_student(stud_dict)
	print(stud_dict == {'tom': 2, 'oxana': 2, 'scoobydoo': 1})


# ============================== END OF FILE =================================

