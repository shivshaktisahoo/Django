# import numpy
# print(np.__version__)                   # check version
                                                    # both are same with alias change
import numpy as np
print(np.__version__)                   # check version

arr = np.array([1,2,3,4,5])
print(type(arr))                        # check type : <class 'numpy.ndarray'>

# Dimensions
arr = np.array(34)
print(arr.ndim)                         # check dimension : 0
arr = np.array([1,2,3,4,5])
print(arr.ndim)                         # this is 1-D

arr = np.array([[1,2,3,5],[4,5,6,6],[7,5,6,7]])
print(arr.ndim)                         # This is 2-D

arr = np.array(
    [
    [[1,2,3,4],[4,5,6,6],[7,5,6,7]],
    [[1,2,3,4],[4,5,6,6],[7,5,6,7]]
    ]
    )
print(arr.ndim)                        # This is 3-D

arr = np.array(
    [
     [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]],
    [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]]
     ]
    )
print(arr.ndim)

# Indexing
print('hai')
print(arr[0,0,2,0])
# print(arr[0][0])
# print(arr[0][0][0])
# print(arr[0][0][0][0])          # 1 will be answwer

# arr = np.array(
#     [
#      [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]],
#     [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]]
#      ]
#     )
# print(arr.sum())                 # for adding everything in matrix


# # Two matrix is adding of 4-D
# arr1 = np.array(
#     [
#      [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]],
#     [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]]
#      ]
#     )
# arr2 = np.array(
#     [
#      [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]],
#     [[[1,2,3,4],[4,5,6,6],[7,5,6,7]],[[1,2,3,4],[4,5,6,6],[7,5,6,7]]]
#      ]
#     )
# print(arr1 + arr2)

# #squareroot
# s = np.sqrt(arr)
# print(s)                        # sqrt of every elements

# # Transpose
# print(arr[0][0])                 # original matrix
# print(arr[0][0].T)               # for Transpose

# # Reshape
# arr = np.array([1,2,3,4,5,6,7,8,9,10])          # 1-D and have 10 elements
# print(arr.reshape(5,2))                         # only reshape b/w their factors
# print(arr.reshape(10,1))
# # print(arr.reshape(3,3))                       # shows an error as elements in arr matrix is 10 but (3,3) for 9 elements

# # min and max
# print(arr.max())                                # maximunm element the that matrix 
# print(arr.min())                                # minimunm element the that matrix

# # argmax and argmin
# arr = np.array([37,8,9,10])                         
# print(arr.argmax())                             # gives position of maximum elememt in that matrix
# print(arr.argmin())                             # gives position of minimum elememt in that matrix

# # range(same as python)---> (arange)
# print(np.arange(50))
# print(np.arange(23,50))
# print(np.arange(23,50,2))

# # we have function zeros and ones only not others like(twos,threes) it shows an error
# print(np.zeros(2))                              # only zeros in matrix, here 2 represents no of elements inside matrix
# print(np.zeros(8))
# print(np.ones(8))                               # only one in matrix
# # print(np.twos(3))                             # error as no attribute in numpy

# # any and all 
# np_array = np.array([False,0,0,0])
# print(np_array.any())                   # In any() function, it (return True) if True values are there or atleast one is present
# np_array = np.array([False,1,0,0])
# print(np_array.any())
   
# np_array = np.array([1,1,1,1])
# print(np_array.all())                   # In all() function, it (return False) if False values are there or atleast one is present
# np_array = np.array([1,1,1,0])
# print(np_array.all())
