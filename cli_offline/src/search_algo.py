

class Search_algo:

    def binary_search_recursion(self, list_values, target_string:str, left_bound:int, right_bound:int) -> int:
        """ practice writing and see how this works.
        Return index of target
        """
        if right_bound <= left_bound:
            return -1

        middle_index:int = (left_bound + right_bound) // 2
        middle_value = list_values[middle_index]


        print(f"DEBUGGING 'result' variable: {middle_value}")
        if middle_value > target_string:
            right_bound = middle_index - 1
            return self.binary_search_recursion(list_values, target_string, left_bound, right_bound)
        elif middle_value < target_string:
            left_bound = middle_index + 1
            return self.binary_search_recursion(list_values, target_string, left_bound, right_bound)
        else:
            return middle_index

    def binary_search_looping(self, list_values, target_string):
        start:int = 0
        end:int = len(list_values)


def find(L, target):
    """ Example from SOF:
            - link: https://stackoverflow.com/a/34327378
    """
    start = 0
    end = len(L) - 1

    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return midpoint
            # return L.index(midpoint)

L = ["Brian", "Joe", "Lois", "Meg", "Peter", "Stewie"] # Needs to be sorted.




if __name__ == "__main__":
    list_values:list[str] = [
    "Adam", 
    "beef", 
    "colobunga", 
    "dude", 
    "eric", 
    "frieza",
    "goku drip",
    ]
    print(find(list_values, "eric"))


    s:Search_algo = Search_algo()
    target_string:str = list_values[4]
    result:int = s.binary_search_recursion(list_values, "eric", 0, len(list_values))
    print(f"Result: {result}")