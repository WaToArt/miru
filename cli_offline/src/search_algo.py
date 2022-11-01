

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
            return self.binary_search_recursion(list_values[middle_index + 1:], target_string)
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
    
    def sequential_search_front_and_end(self, list_values, target_string) -> int: 
        length_list:int = len(list_values)
        middle_index:int = length_list // 2
        for index in range(0, length_list - 1):
            left_side_value = list_values[index]
            
            right_index = ((length_list - 1) - index)
            right_side_value = list_values[right_index]

            if left_side_value == target_string:
                return index
            elif right_side_value == target_string:
                return right_index

            
            if index == middle_index:
                return -1
        
        return -1





if __name__ == "__main__":
    print("Hello :3")