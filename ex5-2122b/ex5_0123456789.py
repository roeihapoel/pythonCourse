''' Exercise #5. Python for Engineers.'''


#########################################
# Question 1 - do not delete this comment
#########################################
def rixum(file_name):
     pass


#########################################
# Question 2 - do not delete this comment
#########################################
def rickounter(f_document, f_rick_identifiers):
    pass


#########################################
# Question 3 - do not delete this comment
#########################################
def twin_pricks(num, out_file_name):
    pass


#########################################
# Question 4 - do not delete this comment
#########################################
def rickode(in_file):
    pass


#########################
# main code - do not delete this comment
# You can add more validation cases below
#########################
if __name__ == "__main__":
    NO_EXC_MSG="Exception must be raised for this input (NOT pass)."
    WRONG_EXC_MSG="Wrong message in raised exception (NOT pass). \nExpected: {}\nGot: {}\n"
    NOT_PASS_MSG="Unexpected result (NOT pass.)"

    PASS_MSG="Got expected results (pass)."
    EXPECTED_EXC_MSG="Got corrent error and error message (pass)."
    

    print('==== Q1: Basic tests/output====')
    q1_input_file_name = "q1_input_1.txt"
    expected_result=137
    actual_result=rixum(q1_input_file_name)
    print("q1t1:", f'{PASS_MSG if expected_result==actual_result else NOT_PASS_MSG}')
    print("TBD: Write more tests here")
    
    print('==== Q2: Basic tests/output====')
    expected_result={'Hello_word9': 0, 'CoolRick11': 1, 'C-137': 2, 'c-132': 1, 'Z0Zo0': 1, 'TestMeRick123': 1}
    actual_result=rickounter("q2_f_document_1.txt", "q2_f_rick_identifiers_1.txt")
    print("q2t1", f"{(PASS_MSG if expected_result==actual_result else NOT_PASS_MSG)}")
    if expected_result!=actual_result:
        print(f'Expected: {expected_result}')
        print(f'Got: {actual_result}')

    print('==== Q3: Basic tests/output====')
    twin_pricks(4, "q3_output_1_res.txt")
    twin_pricks(20, "q3_output_2_res.txt")
    # Compare your output files with the correct output files

    try:
        num = 0
        twin_pricks(num, "q3_output_2_res.txt")  # this line should raise an exception
        print("q3t1", NO_EXC_MSG)
    except ValueError as ex:
        expected_result="Illegal value num={}".format(num)
        actual_result=ex.args[0]
        print(f'{EXPECTED_EXC_MSG if expected_result == actual_result else WRONG_EXC_MSG.format(expected_result , actual_result)}')

    print('==== Q4: Basic tests/output====')
    q4_input_file_name = "q4_input_1.txt"
    deciphered_text="There's a lesson here, and I'm not going to be the one to figure it out\n\nAnd...\n\nThere'Z a lesson here, and I'm not going to be the one to figure it out!!\n"
    with open(rickode(q4_input_file_name),'r') as f:
        print(f'{PASS_MSG if f.read() == deciphered_text else NOT_PASS_MSG}')



   

# ============================== END OF FILE =================================
