# list comprehension
# quickSort, choose first element as pivot
# Huang Jiaming
def quicksort(lst):
    if len(lst) <= 1:
        return lst
    smaller = [x for x in lst[1:] if x < lst[0]]
    larger = [x for x in lst[1:] if x >= lst[0]]
    return quicksort(smaller) + [lst[0]] + quicksort(larger)

if __name__ == '__main__':
    lst = [3,12,9,5,27,1,15,4,3]
    print(quicksort(lst))
