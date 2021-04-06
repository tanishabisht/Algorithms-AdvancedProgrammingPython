# SHARED MEMORY: sharing data between processes


# ----------- #
# USING QUEUE #
# ----------- #

import multiprocessing


def calc_square(nums, q):
    for n in nums:
        q.put(n*n)


if __name__ == '__main__':
    arr = [2,3,5]

    # Creating shared memory
    queue = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=calc_square, args=(arr,queue))

    p1.start()
    p1.join()

    while queue.empty() is False:
        print(queue.get())
    print('Done!')