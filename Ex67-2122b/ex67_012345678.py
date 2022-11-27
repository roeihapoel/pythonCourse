''' Exercise #67. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def threebonacci_rec(n):
    pass #replace this with your implementation


#########################################
# Question 1.b - do not delete this comment
#########################################
def five_bonacci_mem(n, memo=None):
    pass #replace this with your implementation


#########################################
# Question 2.a - do not delete this comment
#########################################
def climb_combinations(n):
    pass #replace this with your implementation


#########################################
# Question 2.b - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    pass #replace this with your implementation


#########################################
# Question 3.a - do not delete this comment
#########################################
def catalan_rec(n):
    pass #replace this with your implementation
    

#########################################
# Question 3.b - do not delete this comment
#########################################
def catalan_memo(n,memo=None):
    pass #replace this with your implementation


#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    pass #replace this with your implementation
    

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    pass #replace this with your implementation


#########################################
# Question 5.a - do not delete this comment
#########################################
def isInTree(tree, val, idx=0):
    pass #replace this with your implementation


#########################################
# Question 5.b - do not delete this comment
#########################################
def create_sorted_binary_tree(lst, tree=None, idx=0):
    pass #replace this with your implementation


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    #Question 1.a tests - you can and should add more    
    """
    print(threebonacci_rec(0) == 0)
    print(threebonacci_rec(5) == 11)
    print(threebonacci_rec(8) == 68)
    """
    #Question 1.b tests - you can and should add more
    """
    print(five_bonacci_mem(0) == 0)
    print(five_bonacci_mem(5) == 10)
    print(five_bonacci_mem(8) == 76)
    """
    #Question 2.a tests - you can and should add more
    """
    print(climb_combinations(4) == 5)
    """
    #Question 2.b tests - you can and should add more
    """
    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)
    """
    #Question 3.a tests - you can and should add more
    """
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    """
    #Question 3.b tests - you can and should add more
    """
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_memo(n) == res)
    """
    #Question 4.a tests - you can and should add more
    """
    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0,[1,2,5,6]) == 1)
    """
    #Question 4.b tests - you can and should add more
    """
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)
    """
    #Question 5.a tests - you can and should add more
    """
    print(isInTree({0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1}, 11) == True)
    print(isInTree({0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1}, 122121) == False)
    print(isInTree({0: 215, 1: 12, 4: 65, 9: 23}, 23) == True)
    """
    #Question 5.b tests - you can and should add more
    """
    print(create_sorted_binary_tree([2, 11, 5, 9, 8, 50, 10, 12, 1]) == {0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1})
    print(create_sorted_binary_tree([215, 12, 65, 23]) == {0: 215, 1: 12, 4: 65, 9: 23})
    print(create_sorted_binary_tree([1, 2, 66, 324, 3122]) == {0: 1, 2: 2, 6: 66, 14: 324, 30: 3122})
    """
    pass
# ============================== END OF FILE =================================
