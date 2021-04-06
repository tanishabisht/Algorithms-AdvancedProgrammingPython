import time
import multiprocessing

square_Result = []

def calc_square(nums):
    global square_Result
    print('Square of the numbers are: ')
    for n in nums:
        time.sleep(0.2)
        print('square: ', n*n)
        square_Result.append(n*n)
        print('Withing process: Result', square_Result)



def calc_cube(nums):
    print('Cube of the numbers are: ')
    for n in nums:
        time.sleep(0.2)
        print('cube: ', n*n*n)



if __name__ == '__main__':
    arr = [2,3,8,9]

    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p2 = multiprocessing.Process(target=calc_cube, args=(arr,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print('Result', square_Result)
    print('Done!')