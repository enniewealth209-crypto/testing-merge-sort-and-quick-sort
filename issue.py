import time
import random


# ==============================
# MERGE SORT
# ==============================

def merge_sort(arr):
    comparisons = 0  # count number of comparisons

    # Recursive divide function
    def divide(lst):
        nonlocal comparisons  # allows us use outer variable

        # Base case: if list has 1 or 0 elements, return it
        if len(lst) <= 1:
            return lst

        # Split list into two halves
        mid = len(lst) // 2
        left = divide(lst[:mid])
        right = divide(lst[mid:])

        # Merge sorted halves
        return merge(left, right)

    # Merge two sorted lists
    def merge(left, right):
        nonlocal comparisons
        result = []
        i = j = 0

        # Compare elements from both halves
        while i < len(left) and j < len(right):
            comparisons += 1  # count comparison

            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Add remaining elements
        result += left[i:]
        result += right[j:]

        return result

    # Start timing
    start = time.time()
    sorted_arr = divide(arr)
    end = time.time()

    # Return number of comparisons and execution time
    return comparisons, end - start


# ==============================
# QUICK SORT
# ==============================

def quick_sort(arr):
    comparisons = 0  # count comparisons

    # Recursive quick sort function
    def divide(lst):
        nonlocal comparisons

        # Base case
        if len(lst) <= 1:
            return lst

        pivot = lst[0]  # choose first element as pivot
        left = []
        right = []

        # Partition elements around pivot
        for x in lst[1:]:
            comparisons += 1  # count comparison

            if x <= pivot:
                left.append(x)
            else:
                right.append(x)

        # Recursively sort left and right
        return divide(left) + [pivot] + divide(right)

    # Start timing
    start = time.time()
    sorted_arr = divide(arr)
    end = time.time()

    # Return comparisons and execution time
    return comparisons, end - start


# ==============================
# GENERATE ARRAY
# ==============================

def generate_array(size, array_type):

    # Random array
    if array_type == 1:
        return [random.randint(1, 1000) for _ in range(size)]

    # Already sorted array (ascending)
    elif array_type == 2:
        return list(range(size))

    # Reverse sorted array (descending)
    elif array_type == 3:
        return list(range(size, 0, -1))


# ==============================
# MAIN PROGRAM (Terminal Menu)
# ==============================

def main():
    print("1. Merge Sort")
    print("2. Quick Sort")

    # Choose algorithm
    choice = int(input("Choose algorithm: "))

    # Enter size of array
    size = int(input("Enter array size: "))

    print("1. Random")
    print("2. Sorted")
    print("3. Reverse")

    # Choose type of input array
    array_type = int(input("Choose array type: "))

    # Generate array
    arr = generate_array(size, array_type)

    # Run selected algorithm
    if choice == 1:
        comp, time_taken = merge_sort(arr)
        print("\nMerge Sort Results")

    elif choice == 2:
        comp, time_taken = quick_sort(arr)
        print("\nQuick Sort Results")

    else:
        print("Invalid choice.")
        return

    # Display performance results
    print(f"Execution Time: {time_taken:.6f} seconds")
    print(f"Comparisons: {comp}")


# Run main only if file is executed directly
if __name__ == "__main__":
    main()
