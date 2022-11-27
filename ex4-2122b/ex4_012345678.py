''' Exercise #4. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def least_popular_characters(my_string):

    pass  # remove this


#########################################
# Question 2 - do not delete this comment
#########################################
def mult_sparse_matrices(lst):

    pass  # remove this


#########################################
# Question 3 - do not delete this comment
#########################################
def fill_substring_dict(s, d, k):
    
    pass  # remove this


#########################################
# Question 4 - do not delete this comment
#########################################
def courses_per_student(tuples_lst):

    pass  # remove this


def num_courses_per_student(stud_dict):

    pass  # remove this

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

