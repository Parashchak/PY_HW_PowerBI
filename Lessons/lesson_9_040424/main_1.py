import numpy

"""
l = [1, 2, 3]
a = numpy.array(l)
print(l*3)
print(a*3)"""

"""arr = numpy.array([[42,7,13],
                   [1,2,3]])
print(arr[0,0:2])"""
"""ltr = [127,55,55]*100000 #-128+127,
print(ltr.__sizeof__())
arr = numpy.array(ltr, dtype='i1')
print(arr.__sizeof__(), type(arr))
newarr = arr.astype('f')
print(newarr)
"""

a = numpy.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]], [[9, 0], [1, 1]]])
# print(a.shape)

# print(a + [1, 20])
a1 = numpy.array([1, 2, 3])
a2 = numpy.array([4, 5, 6])
a3 = numpy.array([1, 2, 3, 4, 5, 6, 3])
print(numpy.concatenate((a1, a2)))  # hstack
print(numpy.stack((a1, a2), axis=1))  # vstack, dstack
print(numpy.array_split(a3, 4))
print(numpy.where(a3 == 3))

arr = numpy.array([8, 4, 3, 12, 20, 55, 2, 1, 4])

arr_n = numpy.array([1, 5, 10])
arr_f = arr
#print(arr[arr_f])

arr_7 = numpy.array([[7, 7, 7], [7, 7, 7], [7, 7, 7]])
print(arr_7)
print(arr_7 * 7)


'''
https://husky-glazer-9f3.notion.site/Materials-a96cd38eae444ac6ac9927d377105245?pvs=4

https://husky-glazer-9f3.notion.site/Before-you-start-00f7cf0438b6493ca08e9ce7611ed02f?pvs=4
'''

import random

"""
arr_n = numpy.random.randint(1, 11, size=(2, 2))
arr_f = arr_n > 5
print(arr_n[arr_f])
arr = numpy.array([[7, 7, 7], [7, 7, 7], [7, 7, 7]])
print(arr)
print(arr * 7)"""

arr_n = numpy.random.randint(1, 100, size=(5, 5, 5))
print(arr_n.flatten())
print(numpy.mean(arr_n))
print(numpy.median(arr_n))

from collections import Counter


def mode(arr: numpy.array):
    all_data = {}
    arr = list(arr.flatten())
    for x in arr:
        if x in all_data:
            all_data.update({x: all_data[x] + 1})
        else:
            all_data.update({x: 1})
    s = sorted(all_data.items(), key=lambda x: x[1], reverse=True)
    s = dict(s)
    return list(s.values())[0]

print(mode(arr_n))