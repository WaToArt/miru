

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




if __name__ == "__main__":
    print("Hello :3")