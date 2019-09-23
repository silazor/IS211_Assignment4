import time
from random import seed
from random import randint
import pprint

def insertion_sort(a_list):
    start = time.time()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    elapsed = end-start
    return elapsed


def shell_sort(a_list):
    start = time.time()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    elapsed = end-start
    return elapsed

def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value


def python_sort(a_list):
    start = time.time()

    a_list.sort()

    end = time.time()
    elapsed = end-start
    return elapsed

def generate_arrays(length):
    seed(1)
    big_array = []
    for _ in range(length):
        value = randint(1, 100)
        big_array.append(value)
    return big_array

def main():
    array_with_500_ints = generate_arrays(500)
    array_with_1000_ints = generate_arrays(1000)
    array_with_10000_ints = generate_arrays(10000)

    total_time = insertion_sort(array_with_500_ints)
    print("Insertion sort 500 took %10.7f seconds to run, on average." %total_time)
    total_time = insertion_sort(array_with_1000_ints)
    print("Insertion sort 1000 took %10.7f seconds to run, on average." %total_time)
    total_time = insertion_sort(array_with_10000_ints)
    print("Insertion sort 10000 took %10.7f seconds to run, on average." %total_time)

    total_time = shell_sort(array_with_500_ints)
    print("Shell sort 500 took %10.7f seconds to run, on average." %total_time)
    total_time = shell_sort(array_with_1000_ints)
    print("Shell sort 1000 took %10.7f seconds to run, on average." %total_time)
    total_time = shell_sort(array_with_10000_ints)
    print("Shell sort 10000 took %10.7f seconds to run, on average." %total_time)

    total_time = python_sort(array_with_500_ints)
    print("Python sort 500 took %10.7f seconds to run, on average." %total_time)
    total_time = python_sort(array_with_1000_ints)
    print("Python sort 1000 took %10.7f seconds to run, on average." %total_time)
    total_time = python_sort(array_with_10000_ints)
    print("Python sort 10000 took %10.7f seconds to run, on average." %total_time)

if __name__ == '__main__':
    main()
