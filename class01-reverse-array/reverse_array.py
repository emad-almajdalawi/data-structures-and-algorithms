x=123

test1 = [1,2,3,4,5,6,7,8,9]
test2 = ['a','b','c','d']
test3 =[1,'a',2,'b', '#', x]

def reverseArray(arr):
    length = 0

    for element in arr:
        length += 1

    i= length -1
    new_arr = []
    while i >= 0 :
        new_arr += [arr[i]]
        i -=1
        
    return new_arr

print(reverseArray(test1))
print(reverseArray(test2))
print(reverseArray(test3))