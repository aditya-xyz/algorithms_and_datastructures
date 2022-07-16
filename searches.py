class Searches:
    def __init__(self) -> None:
        pass

    def binary_search(self, search_list, target):
        first = 0
        last = len(search_list) - 1

        while first <= last:
            midpoint = (first + last) // 2

            if search_list[midpoint] == target:
                return midpoint
            elif search_list[midpoint] < target:
                first = midpoint + 1
            else:
                last = midpoint - 1

    def linear_search(self, search_list, target):
        for i in range(0, len(search_list)):
            if target == search_list[i]:
                return i
        return None

    def recursive_binarysearch(self, search_list, target):
        # A base case is needed to break out of a recursive function
        # This is negative base case
        if len(search_list) == 0:
            return False

        midpoint = len(search_list) // 2

        # This is postive base case
        if search_list[midpoint] == target:
            return True

        # Calling the function recursively until one of the base case is triggered
        if search_list[midpoint] < target:
            return self.recursive_binarysearch(search_list[midpoint + 1 :], target)

        return self.recursive_binarysearch(search_list[: midpoint - 1], target)


s = Searches()
print(f"{s.recursive_binarysearch([1, 2, 3, 4, 5], 5)}")
