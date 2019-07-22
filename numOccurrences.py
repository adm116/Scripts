import sys

''''
    list: list to search
    start: index to start search
    stop: index to stop search
    num: number searched for
    left: boolean value for whether we are searching for the leftmost or
          rightmost occurrence of num

    Recursive solution.

    If left is true, searches the list for the index of the left most occurrence
    of num, otherwise it will search for the index of the right most occurrence
    of num. Returns -1 if the number was not found
'''

def directionalSearch(list, start, stop, num, left):
    # base case
    if start > stop:
        return -1

    mid = (stop + start) // 2
    lastSeen = -1   # track if num is at mid, ie the last guaranteed place we've seen it
    potential = -1  # track num potentially further left or right

    if list[mid] == num: lastSeen = mid

    if left:
        if list[mid] >= num:
            potential = directionalSearch(list, start, mid - 1, num, True)
        else:
            potential = directionalSearch(list, mid + 1, stop, num, True)
    else:
        if list[mid] <= num:
            potential = directionalSearch(list, mid + 1, stop, num, False)
        else:
            potential = directionalSearch(list, start, mid - 1, num, False)

    return potential if potential != -1 else lastSeen

''''
    Returns the number of occurrences of num
'''
def numOccurrences(num, list_):
    left = directionalSearch(list_, 0, len(list_) - 1, num, True)

    if left != -1:
        right = directionalSearch(list_, left, len(list_) - 1, num, False)
        return right - left + 1
    else:
        return 0

''''
    First arg is the number to search for
    Remaining args are the sorted list to search

    Prints the number of occurrences of num.
'''
if __name__ == "__main__":
    num = int(sys.argv[1])

    list_ = []
    for i in range(2, len(sys.argv)):
        list_.append(int(sys.argv[i]))

    print("Found " + str(numOccurrences(num, list_)) + " occurrence(s).")
