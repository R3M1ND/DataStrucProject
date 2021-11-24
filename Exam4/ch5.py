count = 0
def merge(a) -> None :
    # print(a)
    global count
    if len(a) <= 1 :
        return a

    if len(a) > 1 :
        m = len(a) // 2
        left, right = a[:m],a[m:]
        merge(left)
        merge(right)

        i = j = k = 0

        while i < len(left) and j < len(right) :
            count += 1
            if left[i] < right[j] :
                a[k] = left[i]
                i += 1
            else :
                a[k] = right[j]
                j += 1
            k += 1

        while i < len(left) :
            a[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right) :
            a[k] = right[j]
            j += 1
            k += 1

    return a

if __name__ == '__main__' :
    print(' *** Merge sort ***')
    _input = list(map(int, input('Enter some numbers : ').split()))
    # print(_input)
    a = merge(_input)
    print(f'\nSorted -> ', end='')
    print(*a)
    print(f'Data comparison =  {count}')