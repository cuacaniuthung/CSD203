lst = ['A05 Tran Quang 7',
        'A03 Nguyen An 7', 
        'A01 Truong Phung 5',
        'A04 Pham Thi Lam 2',
        'A02 Do Truong Ton 5'
        ]

def bubble_sort(lst, ascending=True):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if (lst[j] > lst[j+1] and ascending) or (lst[j] < lst[j+1] and not ascending):
                lst[j], lst[j+1] = lst[j+1], lst[j]
                swapped = True
        if not swapped:
            break
    
    # In danh sách đã sắp xếp
    if ascending:
        print("Increase:")
    else:
        print("Decrease:")
    
    print('\n'.join(lst))


# Gọi hàm sắp xếp tăng dần
bubble_sort(lst, ascending=True)

# Gọi hàm sắp xếp giảm dần
bubble_sort(lst, ascending=False)
