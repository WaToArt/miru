

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
                end = middle_index # RFER 15
            elif middle_value < target_string:
                start = middle_index + 1
            else:
                return middle_index
    
    def sequential_search_front_and_back(self, list_values, target_string) -> int: # Shorted to sequential_search_fnb
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
    
    def sequential_search_fnb_myanimelist_url_index(self, anime_json, myanimelist_url:str) -> int:
        """
        Search the elements from the front and rear at the same time.
        """
        str_data:str = "data"
        str_sources:str = "sources"

        size_anime_data:int = len(anime_json[str_data])
        middle_index:int = size_anime_data // 2

        for start_index in range(0, size_anime_data - 1):
            start_anime_entry = anime_json[str_data][start_index]
            if myanimelist_url in start_anime_entry[str_sources]:
                return start_index
            
            end_index:int = (size_anime_data - 1) - start_index
            end_anime_entry = anime_json[str_data][end_index]
            if myanimelist_url in end_anime_entry[str_sources]:
                return end_index

            if start_index == middle_index:
                return -1
        
        return -1

    def sequential_search_fnb_myanimelist_url_anime_info(self, anime_json, myanimelist_url:str):
        """
        Search the elements from the front and rear at the same time.
        """
        str_data:str = "data"
        str_sources:str = "sources"

        size_anime_data:int = len(anime_json[str_data])
        middle_index:int = size_anime_data // 2

        for start_index in range(0, size_anime_data - 1):
            start_anime_entry = anime_json[str_data][start_index]
            if myanimelist_url in start_anime_entry[str_sources]:
                return start_anime_entry
            
            end_index:int = (size_anime_data - 1) - start_index
            end_anime_entry = anime_json[str_data][end_index]
            if myanimelist_url in end_anime_entry[str_sources]:
                return end_anime_entry

            if start_index == middle_index:
                return {}
        
        return {}





if __name__ == "__main__":
    print("Hello :3")