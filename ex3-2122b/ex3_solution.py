''' Exercise #3. Python for Engineers.'''

#########################################
# Question 1 - do not delete this comment
#########################################
def mult_residuals_of_k(lst, k):
    multiply = 1.0
    for item in lst:
        if not item % k == 0:
            multiply *= item % k
    return multiply

print(mult_residuals_of_k([45,60,74,48],1))

#########################################
# Question 2 - do not delete this comment
#########################################
def sum_even_digits(n):
    str_n = str(n)
    sum_even = 0
    for c in str_n:
        if int(c) % 2 == 0 :
            sum_even += int(c)
    return sum_even

print(sum_even_digits(54984127))

#########################################
# Question 3 - do not delete this comment
#########################################
def count_longest_repetition(s, c):

    s = s.lower()
    max_seq = 0
    for i in range(len(s)):
        if s[i] == c:
            current_seq = 0
            for j in range(i, len(s)):
                if s[j] == c:
                    current_seq += 1
                else:
                    break
            if current_seq > max_seq:
                max_seq = current_seq
    return max_seq

print(count_longest_repetition("CCCccc", 'c'))



#########################################
# Question 4 - do not delete this comment
#########################################

def lower_strings(lst):
    if type(lst) != list:
        return -1
    new_lst = []
    for i in range(len(lst)):
        if type(lst[i]) == str:
            lst[i] = lst[i].lower()

vals = [11, 'Rick137', 3.14, 'MoRTy']
result = lower_strings(vals)
print(vals)
print(result)
#########################################
# Question 5 - do not delete this comment
#########################################
def mult_mat_by_scalar(mat, alpha):

    new_mat = []
    for row in mat:
        new_row = []
        for item in row:
            new_row.append(item * alpha)
        new_mat.append(new_row)
    return new_mat

mat1 = [[2, 5], [6, 9]]
mat2 = mult_mat_by_scalar(mat1, 2)
print(mat2)


#########################################
# Question 6 - do not delete this comment
#########################################
def mat_transpose(mat):
    new_mat = []
    num_of_cols = len(mat[0])
    for i in range(num_of_cols):
        new_row = []
        for j in range(len(mat)):
            new_row.append(mat[j][i])
        new_mat.append(new_row)
    return new_mat

print(mat_transpose( [[0, 1, 2], [10, 11, 12], [20, 21, 22]]))


    
#########################
# main code - do not delete this comment
# Tests have been added for your convenience.
# You can add more tests below.
#########################
if __name__ == '__main__':  # Do not delete this line!
    print(mult_residuals_of_k([3, 6, 4, 11, 9], 3) == 2.0 )
    print(mult_residuals_of_k([45.5, 60, 74, 48], 4) == 3.0)


    print(sum_even_digits(5638) == 14)
    print(sum_even_digits(137) == 0)
    print(sum_even_digits(54984127) == 18)
    print(sum_even_digits(6) == 6)


    print(count_longest_repetition('eabbaaaacccaaddd', 'a') == 4)
    print(count_longest_repetition('cccccc','c') == 6)
    print(count_longest_repetition('abcde', 'z') == 0)


    vals = [11, 'Rick137', 3.14, 'moRTy']
    result=lower_strings(vals)
    print(vals == [11, 'rick137', 3.14, 'morty'])
    print(result == None)

    vals = [-5, None, True, [1, 'dont change me', 3]]
    lower_strings(vals)
    print(vals == [-5, None, True, [1, 'dont change me', 3]])

    print(lower_strings(42) == -1)
    print(lower_strings('im not a list') == -1)
    print(lower_strings(False) == -1)


    mat1 = [[2, 5], [6, 9]]
    mat2 = mult_mat_by_scalar(mat1, 2)
    print(mat1 == [[2, 5], [6, 9]])
    print(mat2 == [[4, 10], [12, 18]])

    print(mult_mat_by_scalar([[10,15], [-3,6]], -5) == [[-50, -75], [15, -30]])


    mat = [[1,2],[3,4],[5,6]]
    mat_T = mat_transpose(mat)
    print(mat == [[1, 2], [3, 4], [5, 6]])
    print(mat_T == [[1, 3, 5], [2, 4, 6]])

    mat2 = [[0, 1, 2], [10, 11, 12], [20, 21, 22]]
    mat2_T = mat_transpose(mat2)
    print(mat2_T == [[0, 10, 20], [1, 11, 21], [2, 12, 22]])


# ============================== END OF FILE =================================
