def find_common_elements(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    common = list(set1.intersection(set2))  # Convert intersection back to a list
    return common
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result= find_common_elements(list1, list2)
print(f"The common elements are: {result}")