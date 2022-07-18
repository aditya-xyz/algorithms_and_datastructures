class Sorts:
    def __init__(self) -> None:
        pass

    def merge_sort(self, values):
        if len(values) <= 1:
            return values
        # divide: find mid point of list and divide into sublists
        midpoint = len(values) // 2
        left_half = values[:midpoint]
        right_half = values[midpoint:]

        # conquer: recursively sort sublists in ascending order
        self.merge_sort(left_half)
        self.merge_sort(right_half)

        # combine: merge sorted sublists
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                values[k] = left_half[i]
                i += 1
            else:
                values[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            values[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            values[k] = right_half[j]
            j += 1
            k += 1
        return values

    def quick_sort(self, values):
        if len(values) <= 1:
            return values

        values_less_than_pivot = []
        values_greater_than_pivot = []
        pivot = values[0]

        for value in values[1:]:
            if value <= pivot:
                values_less_than_pivot.append(value)
            else:
                values_greater_than_pivot.append(value)

        return (
            self.quick_sort(values_less_than_pivot)
            + [pivot]
            + self.quick_sort(values_greater_than_pivot)
        )


s = Sorts()
list_to_sort = [23, 1, 55, 99, 203, 2, 5, 34]
sorted_list = s.quick_sort(list_to_sort)

print(sorted_list)
