# # # # lst = [1, 2, 3, 4, 1, 3, 5]
# # # # lst.extend(lst)
# # # # print(lst)
# # # # set1 = set(lst)

# # # # print(set1)

# # # # st = set()

# # # # st.update(lst)

# # # # print(st)

# # # # Write your code here.
# # # def add_to_set(st, lst):
# # #     return st.union(set(lst))

# # # st = { 1, 2, 3, 4 }
# # # lst = [12, 4, 42, 93, 2, 85]

# # # print(add_to_set(st, lst))    # { 1, 2, 3, 4, 42, 12, 85, 93 }

# # # Write your code here.
# # def left_diff(set1, set2):
# #     return set1 - set2



# # set1 = { 1, 2, 5, 10 }
# # set2 = { 2, 6, 10, 12 }

# # print(left_diff(set1, set2))    # { 1, 5 }

# # Write your code here.
# def remove_repeats(str1, str2):
#     set1 = set(set(str1))
#     set2 = set(set(str2))
#     common_set = set1 | set2
#     common_items = set1 & set2
#     return common_set - common_items


# str1 = 'aloha'
# str2 = 'bonjour'

# print(remove_repeats(str1, str2))    # {'r', 'a', 'l', 'h', 'n', 'b', 'j', 'u'}

# Write your code here.
def check_binary(str):
    str_set = set(str)
    return str_set == { '0', '1' } or str_set == { '1' } or str_set == { '0' }

    

str1 = '1010001010010100101'
str2 = '1010010015010101010'

print(check_binary(str1))       # True
print(check_binary(str2))       # False

