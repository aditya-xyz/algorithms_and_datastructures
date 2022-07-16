from linkedlist import LinkedList


class Sorts:
    def __init__(self) -> None:
        pass

    def merge_sort(self, unsorted_list):
        if len(unsorted_list) <= 1:
            return
        # divide: find mid point of list and divide into sublists
        midpoint = len(unsorted_list) // 2
        left_half = unsorted_list[:midpoint]
        right_half = unsorted_list[midpoint:]

        # conquer: recursively sort sublists in ascending order
        self.merge_sort(left_half)
        self.merge_sort(right_half)

        # combine: merge sorted sublists
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                unsorted_list[k] = left_half[i]
                i += 1
            else:
                unsorted_list[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            unsorted_list[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            unsorted_list[k] = right_half[j]
            j += 1
            k += 1


s = Sorts()
list_to_sort = LinkedList([23, 1, 55, 99, 203, 2, 5, 34])
s.merge_sort_linkedlist(list_to_sort)

print(list_to_sort)
