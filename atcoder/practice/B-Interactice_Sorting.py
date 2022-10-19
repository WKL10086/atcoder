import sys
import string

askDict = {}


def get_arrow(str1, str2):
    ask = "? " + str1 + " " + str2

    if ask in askDict:
        arrow = askDict[ask]
    else:
        print("? " + str1 + " " + str2)
        sys.stdout.flush()
        arrow = input()
        askDict[ask] = arrow

    return arrow


def merge_sort(list):
    # 1. Store the length of the list
    list_length = len(list)

    # 2. List with length less than is already sorted
    if list_length == 1:
        return list

    # 3. Identify the list midpoint and partition the list into a left_partition and a right_partition
    mid_point = list_length // 2

    # 4. To ensure all partitions are broken down into their individual components,
    # the merge_sort function is called and a partitioned portion of the list is passed as a parameter
    left_partition = merge_sort(list[:mid_point])
    right_partition = merge_sort(list[mid_point:])

    # 5. The merge_sort function returns a list composed of a sorted left and right partition.
    return merge(left_partition, right_partition)


# 6. takes in two lists and returns a sorted list made up of the content within the two lists
def merge(left, right):
    # 7. Initialize an empty list output that will be populated with sorted elements.
    # Initialize two variables i and j which are used pointers when iterating through the lists.
    output = []
    i = j = 0

    # 8. Executes the while loop if both pointers i and j are less than the length of the left and right lists
    while i < len(left) and j < len(right):
        # 9. Compare the elements at every position of both lists during each iteration
        arrow = get_arrow(left[i], right[j])

        if arrow == "<":
            # output is populated with the lesser value
            output.append(left[i])
            # 10. Move pointer to the right
            i += 1
        else:
            output.append(right[j])
            j += 1
    # 11. The remnant elements are picked from the current pointer value to the end of the respective list
    output.extend(left[i:])
    output.extend(right[j:])

    return output


def run_26_merge_sort():
    unsorted_list = list(string.ascii_uppercase[:26])

    sorted_list = merge_sort(unsorted_list)

    print("! " + "".join(sorted_list))
    sys.stdout.flush()


def sort5(a, b, c, d, e):
    if get_arrow(a, b) == "<":
        a, b = b, a
    if get_arrow(c, d) == "<":
        c, d = d, c
    if get_arrow(a, c) == "<":
        a, b, c, d = c, d, a, b
    if get_arrow(e, c) == "<":
        if get_arrow(e, d) == "<":
            pass
        else:
            d, e = e, d
    else:
        if get_arrow(e, a) == "<":
            c, d, e = e, c, d
        else:
            a, c, d, e = e, a, c, d
    if get_arrow(b, d) == "<":
        if get_arrow(b, e) == "<":
            return b, e, d, c, a
        else:
            return e, b, d, c, a
    else:
        if get_arrow(b, c) == "<":
            return e, d, b, c, a
        else:
            return e, d, c, b, a


def run_5_sort():
    unsorted_list = list(string.ascii_uppercase[:5])

    sorted_list = list(
        sort5(
            unsorted_list[0],
            unsorted_list[1],
            unsorted_list[2],
            unsorted_list[3],
            unsorted_list[4],
        )
    )

    print("! " + "".join(sorted_list))
    sys.stdout.flush()


def init():
    N, Q = input().split()
    if int(N) == 26:
        run_26_merge_sort()
    else:
        run_5_sort()


init()
