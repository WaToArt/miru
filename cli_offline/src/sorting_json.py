
class sorting_json:
    def __init__(self) -> None:
        pass

    def sort_by_MAL_url(self, response_json):
        output_json:dict = response_json

        ### Finish writing code #TODO

        print(sorted(output_json['data'], key=lambda item: item['sources'].split()[-1]))

        return output_json