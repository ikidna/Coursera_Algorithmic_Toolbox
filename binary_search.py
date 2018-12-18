# Uses python3
import sys

'''
def binary_search(a, x):
    left, right = 0, len(a)
    # write your code here
'''

def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1

def binary_search_recursive(a, l, r, x):
    if r >=l:
        mid = (l+r)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search_recursive(a, l, mid-1, x)
        else:
            return binary_search_recursive(a, mid+1, r, x)


def binary_search(a, m, x):
    first = 0
    last = m - 1
    while first <= last: 
        mid  = (first + last)//2
        if x == a[mid]:
            return mid
        elif x > a[mid]:
            first = mid + 1
        else:
            last = mid - 1
    return -1


'''
#data = (5, 1, 5, 8, 12, 13, 5, 8, 1, 23, 1, 11)
#data = (5, 1, 2, 3, 4, 5, 5, 1, 2, 3, 4, 5)
data = (0, 0)
n = data[0]
m = data[n + 1]
a = data[1 : n + 1]
for x in data[n + 2:]:
    print(binary_search(a, m, x), end = ' ')
'''


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        # replace with the call to binary_search when implemented
        print(binary_search(a, m, x), end = ' ')
