

class Search_algo:

    def binary_search_recursion(self, list_values, target_string:str) -> int: # RFER 13
        
        if len(list_values) == 0:
            return -1

        middle_index:int = len(list_values) // 2
        middle_value = list_values[middle_index]

        print(f"DEBUGGING 'result' variable: {middle_value}")
        if middle_value > target_string:
            return self.binary_search_recursion(list_values[:middle_index], target_string)
        elif middle_value < target_string:
            return self.binary_search_recursion(list_values[middle_index:], target_string)
        else:
            return middle_value

    def binary_search_looping(self, list_values, target_string): # RFER 14
        start:int = 0
        end:int = len(list_values) - 1

        while start <= end:
            middle_index:int = (start + end) // 2
            middle_value = list_values[middle_index]

            if middle_value > target_string:
                end = middle_index - 1
            elif middle_value < target_string:
                start = middle_index + 1
            else:
                return middle_index




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