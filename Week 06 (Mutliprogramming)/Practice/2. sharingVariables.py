# SHARED MEMORY: sharing data between processes


# ----------- #
# USING ARRAY #
# ----------- #

# import time
# import multiprocessing


# def calc_square(nums, res):
#     for idx,n in enumerate(nums):
#         res[idx] = (n*n)


# if __name__ == '__main__':
#     arr = [2,3,5]

#     # Creating shared memory
#     result = multiprocessing.Array('i',3)

#     p1 = multiprocessing.Process(target=calc_square, args=(arr,result))

#     p1.start()
#     p1.join()

#     print('outside process: ', result[:])
#     print('Done!')






# ----------- #
# USING VALUE #
# ----------- #

import time
import multiprocessing


def calc_square(nums, res, value):
    value.value = 5.67
    for idx,n in enumerate(nums):
        res[idx] = (n*n)


if __name__ == '__main__':
    arr = [2,3,5]

    # Creating shared memory
    result = multiprocessing.Array('i',3)
    value = multiprocessing.Value('d',0.0)

    p1 = multiprocessing.Process(target=calc_square, args=(arr,result,value))

    p1.start()
    p1.join()

    print('outside process: ', result[:])
    print('Value: ', value.value)
    print('Done!')