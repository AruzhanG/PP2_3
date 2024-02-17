def unique (list1):
    list1 = list(map(int, list1.split()))
    unique_list = []
    
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
            
    for x in unique_list:
        print(x)
        
"""list1 = [12,3,4,5,12,3]
unique(list1)"""
user_input = input()
unique(user_input)
