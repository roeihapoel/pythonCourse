''' Exercise #67. Python for Engineers.'''

#########################################
# Question 1.a - do not delete this comment
#########################################
def threebonacci_rec(n):
    if n <= 2:
        return n
    return threebonacci_rec(n-1) + threebonacci_rec(n-2) + threebonacci_rec(n-3)

#########################################
# Question 1.b - do not delete this comment
#########################################
def five_bonacci_mem(n, memo=None):
    if n <= 4:
        return n
    if memo is None:
        memo = {}
    if memo.get(n) is None:
        memo[n] = five_bonacci_mem(n-1, memo) + five_bonacci_mem(n-2, memo) + five_bonacci_mem(n-3, memo) + five_bonacci_mem(n-4, memo) + five_bonacci_mem(n-5, memo)
    return memo[n]

#########################################
# Question 2.a - do not delete this comment
#########################################
def climb_combinations(n):
    if n == 1 or n==0:
        return 1
    return climb_combinations(n-1) + climb_combinations(n-2)

#########################################
#########################################
# Question 2.b - do not delete this comment
#########################################
def climb_combinations_memo(n, memo=None):
    if n == 1 or n==0:
        return 1
    if memo is None:
        memo = {}
    if memo.get(n) is None:
        memo[n] = climb_combinations_memo(n-1, memo) + climb_combinations_memo(n-2, memo)
    return memo[n]
#########################################
# Question 3.a - do not delete this comment
#########################################
def catalan_rec(n):
    if n==0:
        return 1
    x = 0
    for i in range(n):
        x += catalan_rec(i) * catalan_rec(n-1-i)
    return x

#########################################
# Question 3.b - do not delete this comment
#########################################
def catalan_memo(n,memo=None):
    if n == 0:
        return 1

    if memo is None:
        memo = {}
    x = 0
    for i in range(n):
        if memo.get(i) is None:
            memo[i] = catalan_memo(i, memo)
        if memo.get(n-1-i) is None:
            memo[n-i-1] = catalan_memo(n-i-1, memo)
        x += memo[i] * memo[n-1-i]
    return x

#########################################
# Question 4.a - do not delete this comment
#########################################
def find_num_changes_rec(n, lst):
    if (lst == [] and n > 0) or n < 0:
        return 0
    if n == 0:
        return 1
    if lst[-1] <= n:
        return find_num_changes_rec(n - lst[-1], lst) + find_num_changes_rec(n, lst[:-1])
    return find_num_changes_rec(n, lst[:-1])

#########################################
# Question 4.b - do not delete this comment
#########################################
def find_num_changes_mem(n, lst, memo=None):
    if (lst == [] and n > 0) or n < 0:
        return 0
    if n == 0:
        return 1
    if memo is None:
        memo = {}
    if memo.get((n, len(lst))) is None:
        if lst[-1] <= n:
            memo[(n, len(lst))] = find_num_changes_mem(n - lst[-1], lst, memo) + find_num_changes_mem(n, lst[:-1], memo)
        else:
            memo[(n, len(lst))] = find_num_changes_mem(n, lst[:-1], memo)
    return memo[(n, len(lst))]


#########################################
# Question 5.a - do not delete this comment
#########################################
def isInTree(tree, val, idx=0):
    if tree.get(idx) is None:
        return False
    if tree.get(idx) == val:
        return True
    return isInTree(tree, val, 2*idx +1) or isInTree(tree, val, 2 * idx + 2)


#########################################
# Question 5.b - do not delete this comment
#########################################

def create_sorted_binary_tree_get_index(item, tree, idx=0):
    if tree is None or tree.get(idx) is None:
        return idx
    else:
        if item > tree[idx]:
            return create_sorted_binary_tree_get_index(item, tree, 2 * idx + 2 )
        else:
            return  create_sorted_binary_tree_get_index(item, tree, 2 * idx + 1)

def create_sorted_binary_tree(lst, tree=None, idx=0):
    if lst == []:
        return None
    if tree is None:
        tree = {}
    index = create_sorted_binary_tree_get_index(lst[0], tree, idx)
    tree[index] = lst[0]
    if len(lst)>0:
        create_sorted_binary_tree(lst[1:], tree, 0)
    return tree

#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    #Question 1.a tests - you can and should add more    

    print(threebonacci_rec(0) == 0)
    print(threebonacci_rec(5) == 11)
    print(threebonacci_rec(8) == 68)

    #Question 1.b tests - you can and should add more

    print(five_bonacci_mem(0) == 0)
    print(five_bonacci_mem(5) == 10)
    print(five_bonacci_mem(8) == 76)

    #Question 2.a tests - you can and should add more

    print(climb_combinations(4) == 5)

    #Question 2.b tests - you can and should add more

    print(climb_combinations_memo(4) == 5)
    print(climb_combinations_memo(42) == 433494437)

    #Question 3.a tests - you can and should add more
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_rec(n) == res)
    #Question 3.b tests - you can and should add more
    cat_list = [1,1,2,5,14,42,132,429]
    for n,res in enumerate(cat_list):
        print(catalan_memo(n) == res)
    #Question 4.a tests - you can and should add more

    print(find_num_changes_rec(5,[1,2,5,6]) == 4)
    print(find_num_changes_rec(4,[1,2,5,6]) == 3)
    print(find_num_changes_rec(0,[1,2,5,6]) == 1)

    #Question 4.b tests - you can and should add more
    print(find_num_changes_mem(5,[1,2,5,6]) == 4)
    print(find_num_changes_mem(4,[1,2,5,6]) == 3)
    print(find_num_changes_mem(105,[1,105,999,100]) ==3)

    #Question 5.a tests - you can and should add more

    print(isInTree({0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1}, 11) == True)
    print(isInTree({0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1}, 122121) == False)
    print(isInTree({0: 215, 1: 12, 4: 65, 9: 23}, 23) == True)

    #Question 5.b tests - you can and should add more

    print(create_sorted_binary_tree([2, 11, 5, 9, 8, 50, 10, 12, 1]) == {0: 2, 2: 11, 5: 5, 12: 9, 25: 8, 6: 50, 26: 10, 13: 12, 1: 1})
    print(create_sorted_binary_tree([215, 12, 65, 23]) == {0: 215, 1: 12, 4: 65, 9: 23})
    print(create_sorted_binary_tree([1, 2, 66, 324, 3122]) == {0: 1, 2: 2, 6: 66, 14: 324, 30: 3122})

    pass
# ============================== END OF FILE =================================
