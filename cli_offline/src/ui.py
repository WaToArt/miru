from parse_info import parsed_anime_database

class user_interface:

    def __init__(self) -> None:
        self.parsing_anime_database:parsed_anime_database = parsed_anime_database()
        self.main_menu_options:list[str] = ["Type in one of the options!",
            "1) hello",
            "2) download",
        ]
        

    def start_program(self):
        while True:
            for option in self.main_menu_options:
                print(option)

            input_command:str = input('>> ')
            print()

            match input_command.lower().strip():
                case 'quit':
                    print('Now quitting program.')
                    break
                case '2' | 'download':
                    print('you chosen download')
                case other:
                    print('That was not option :\'\[')
            
            print("=========\n")

    def verify_downloaded_json(self) -> bool:
        pass
    
if __name__ == '__main__':
    ui = user_interface()
    ui.start_program()
