import time
from random import seed
from random import randint
import pprint

def sequential_search(big_list, item):
    start = time.time()
    for a_list in big_list:
        # These are initializers
        pos = 0
        found = False
        # do the stuff belove
        # This loops through a single array
        while pos < len(a_list) and not found:
            if a_list[pos] == item:
                found = True
                end = time.time()
                elapsed = end-start
                return (found, elapsed)
            else:
                pos = pos+1
    end = time.time()
    elapsed = end-start

    return(found, elapsed)

def ordered_sequential_search(big_list, item):
    start = time.time()
    for ordered_sequential_list in big_list:
        pos = 0
        found = False
        stop = False
        while pos < len(ordered_sequential_list) and not found and not stop:
            if ordered_sequential_list[pos] == item:
                found = True
                end = time.time()
                elapsed = end-start
                return (found, elapsed)
            else:
                if ordered_sequential_list[pos] > item:
                    stop = True
                else:
                    pos = pos+1
    end = time.time()
    elapsed = end-start
    return(found, elapsed)

def binary_search():
    start = time.time()
    #code
    end = time.time()
    elapsed = end-start
    pass

def binary_search_recursive(binary_recursive_list, item):
    if len(binary_recursive_list) == 0:
        return False
    else:
        midpoint = len(binary_recursive_list)//2
        if binary_recursive_list[midpoint] == item:
            return True
        else:
            if item < binary_recursive_list[midpoint]:
                return binary_search_recursive(binary_recursive_list[:midpoint], item)
            else:
                return binary_search_recursive(binary_recursive_list[midpoint + 1:], item)

def generate_arrays(length):
    seed(1)
    big_ol_array = []
    for num in range(0, 100):
        lil_array_holder = []
        for _ in range(length):
            value = randint(1, 100)
            lil_array_holder.append(value)
        big_ol_array.append(lil_array_holder)
    return big_ol_array

def sorted_list(big_list):
    new_big_list = []
    for little_list in big_list:
        little_list.sort()
        new_big_list.append(little_list)
    return new_big_list

def binary_search_iterative(big_list, item):
    start = time.time()
    for binary_iterative_list in big_list:
        first = 0
        last = len(binary_iterative_list) - 1
        found = False
        while first <= last and not found:
            midpoint = (first + last) // 2
            if binary_iterative_list[midpoint] == item:
                found = True
                end = time.time()
                elapsed = end-start
                return(found, elapsed)
            else:
                if item < binary_iterative_list[midpoint]:
                    last = midpoint - 1
                else:
                    first = midpoint + 1
    end = time.time()
    elapsed = end-start
    return(found, elapsed)

def main():
    results = {}
    array_100_with_500_ints = generate_arrays(500)
    array_100_with_1000_ints = generate_arrays(1000)
    array_100_with_10000_ints = generate_arrays(10000)

    sorted_500 = sorted_list(array_100_with_500_ints)
    sorted_1000 = sorted_list(array_100_with_1000_ints)
    sorted_10000 = sorted_list(array_100_with_10000_ints)

    found, total_time = sequential_search(array_100_with_500_ints, -1)
    print("Sequential search 500 took %10.7f seconds to run, on average." %total_time)
    found, total_time = sequential_search(array_100_with_1000_ints, -1)
    print("Sequential search 1000 took %10.7f seconds to run, on average." %total_time)
    found, total_time = sequential_search(array_100_with_10000_ints, -1)
    print("Sequential search 10000 took %10.7f seconds to run, on average." %total_time)

    found, total_time = ordered_sequential_search(sorted_500, -1)
    print("Ordered sequential search 500 took %10.7f seconds to run, on average." %total_time)
    found, total_time = ordered_sequential_search(sorted_1000, -1)
    print("Ordered sequential search 1000 took %10.7f seconds to run, on average." %total_time)
    found, total_time = ordered_sequential_search(sorted_10000, -1)
    print("Ordered sequential search 10000 took %10.7f seconds to run, on average." %total_time)

    found, total_time = binary_search_iterative(sorted_500, -1)
    print("Binary search iterative 500 took %10.7f seconds to run, on average." %total_time)
    found, total_time = binary_search_iterative(sorted_1000, -1)
    print("Binary search iterative 1000 took %10.7f seconds to run, on average." %total_time)
    found, total_time = binary_search_iterative(sorted_10000, -1)
    print("Binary search iterative 10000 took %10.7f seconds to run, on average." %total_time)

    start = time.time()
    for list in sorted_500:
        binary_search_recursive(list, -1)
    end = time.time()
    elapsed = end-start
    print("Binary search recursive 500 took %10.7f seconds to run, on average." %elapsed)

    start = time.time()
    for list in sorted_1000:
        binary_search_recursive(list, -1)
    end = time.time()
    elapsed = end-start
    print("Binary search recursive 1000 took %10.7f seconds to run, on average." %elapsed)

    start = time.time()
    for list in sorted_1000:
        binary_search_recursive(list, -1)
    end = time.time()
    elapsed = end-start
    print("Binary search recursive 10000 took %10.7f seconds to run, on average." %elapsed)

if __name__ == '__main__':
    main()
