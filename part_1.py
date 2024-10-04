lst = ['A05 Tran Quang 7',
        'A03 Nguyen An 7', 
        'A01 Truong Phung 5',
        'A04 Pham Thi Lam 2',
        'A02 Do Truong Ton 5'
        ]

# bubble
# for i in range(1, len(lst)):
#     current_value = lst[i]
#     insert_index = i - 1


#     while insert_index >= 0 and lst[insert_index] > current_value:
#         lst[insert_index + 1] = lst[insert_index]
#         insert_index -= 1

#     lst[insert_index + 1] = current_value




# selection

# for i in range(len(lst)):
#     min_index = i

#     for j in range(i+1, len(lst)):
#         if lst[j] < lst[min_index]: 
#             min_index = j


#     lst[i], lst[min_index] = lst[min_index], lst[i]


# bubble

for i in range(len(lst)):
    swapped = False
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j+1]:
            lst[j], lst[j+1] = lst[j+1], lst[j]
            swapped = True
    if not swapped:
        break

print('\n'.join(lst))