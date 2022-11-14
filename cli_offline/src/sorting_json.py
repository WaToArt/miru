import json


class sorting_json:
    def __init__(self) -> None:
        pass

    def sort_by_MAL_url(self, response_json):

        """### Finish writing code #TODO

        - obtain data from json and assign to variable 'dict_json_data'
            - since json is a list, sort by MAL url
        - replace 'response_json''s 'data' with sorted 'dict_json_data' 

        """
        print("\n\n ====== assigning variable for json's data ======\n")
        dict_json_data:list = (response_json['data'])
        print(f"assigned content of 'data' to variable 'dict_json_data'")
        
        print("\n\n=== sorted data === \n")

        dict_json_data.sort(key=lambda item: item['sources'])
        print(json.dumps(dict_json_data, indent=2))
        
        print("\n\n ====== output_json ====== \n")
        output_json = dict_json_data
        print(output_json)

        print("\n=======new line========\n")

        print(json.dumps(output_json, indent=2))
        return output_json