""" Exercise #2. Python for Engineers."""

#########################################
# Question 1 - do not delete this comment
#########################################

a = 2  # Replace the assignment with a positive integer to test your code.
lst = [1, 2, 3, 4, 5, 6,7]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 1 below here.


counter = 0
for i in range(len(lst)):
    if lst[i] % a == 0:
        counter += 1
    if counter == 3:
        print(i)
        break
if counter < 3:
    print(-1)

# End of code for question 1

#########################################
# Question 2 - do not delete this comment
#########################################
lst2 = ['rick', 'and', 'morty']
# Replace the assignment with other lists of strings (str) to test your code.


# Write the code for question 2 using a for loop below here.

summer_len = 0
for item in lst2:
    summer_len += len(item)
avg_len = summer_len / len(lst2)
counter_items = 0
for item in lst2:
    if len(item) > avg_len:
        counter_items += 1
print("The number of strings longer than the average is:" , str(counter_items))

# Write the code for question 2 using a while loop below here.

summer_len = 0
i = 0
while i < len(lst2):
    summer_len += len(lst2[i])
    i+=1
avg_len = summer_len / len(lst2)
counter_items = 0
i = 0
while i < len(lst2):
    if len(lst2[i]) > avg_len:
        counter_items += 1
    i+=1
print("The number of strings longer than the average is:" , str(counter_items))


# End of code for question 2

#########################################
# Question 3 - do not delete this comment
#########################################

lst3 = [0, 1,  4, 3]  # Replace the assignment with other lists to test your code.

# Write the rest of the code for question 3 below here.

deltas = []
for i in range(len(lst3) - 1 ):
    deltas.append(abs(lst3[i] - lst3[i+1]))
print(sum(deltas))



# End of code for question 3


#########################################
# Question 4 - do not delete this comment
#########################################

lst4 = [1, -4, 2,  2, 3, -9, 10]  # Replace the assignment with other lists to test your code.
# Write the rest of the code for question 4 below here.


new = []
new.append(lst4[0])
new.append(lst4[1])
for i in range(2, len(lst4)):
    current_multiply = abs(lst4[i] * lst4[i - 1])
    to_check = True
    for j in range(0,i-1):
        if abs(lst4[j] * lst4[j+1]) > current_multiply:
            to_check = False
            break
    if to_check:
        new.append(lst4[i])
print(new)

# End of code for question 4

#########################################
# Question 5 - do not delete this comment
#########################################

my_string = 'abaadddefffgg'  # Replace the assignment with other strings to test your code.
k = 3  # Replace the assignment with a positive integer to test your code.

# Write the rest of the code for question 5 below here.


if len(my_string) == 0:
    print("Didn't find a substring of length", k)
all_k_strings = []
current_char = my_string[0]
current_length = 1
for i in range(1, len(my_string)):
    if current_length == k:
        all_k_strings.append(current_char * k)
    if my_string[i] == current_char:
        current_length += 1
    else:
        current_char = my_string[i]
        current_length = 1
if current_length == k:
    all_k_strings.append(current_char * k)
if len(all_k_strings) == 0:
    print("Didn't find a substring of length", k)
else:
    max_char = all_k_strings[0][0]
    for item in all_k_strings:
        if item[0] > max_char:
            max_char = item[0]
    print("For length {}, found the substring {}!".format(k,max_char*k))


# End of code for question 5
