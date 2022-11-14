import json


class sorting_json:
    def __init__(self) -> None:
        pass

    def sort_by_MAL_url(self, response_json):
        output_json:dict = response_json

        ### Finish writing code #TODO

        output_json = sorted(output_json.items(), key=lambda item: item['data']['sources'])
        print(output_json)

        print("\n=======new line========\n")

        print(json.dumps(output_json, indent=4))
        return output_json