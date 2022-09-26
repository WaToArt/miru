from parse_info import parsed_anime_database

class user_interface:

    def __init__(self) -> None:
        self.parsing_anime_database:parsed_anime_database = parsed_anime_database()
        
        

    def start_program(self):
        while True:
            print("Here are your options!")
            print("Type the worded option!")
            main_menu_options:list[str] = [
                 
                "Roll",
                "download",
                "stats",



                "quit",
            ]

            for index, item in enumerate(main_menu_options):
                # print(f"{index}): {item}")
                print(f"* {item}")

            input_command:str = input('>> ')
            print()

            match input_command.lower().strip():
                case 'quit':
                    print('Now quitting program.')
                    break
                case 'download' :
                    self.download_json()
                case 'stats':
                    self.stats_info()
                case other:
                    print('Warning: That was not option :\'\[. Please try again.')
            
            print("=========\n")

    def stats_info(self):
        print('you chosen stats')

    def download_json(self) -> bool:
        print('you chosen download')

    
if __name__ == '__main__':
    ui = user_interface()
    ui.start_program()
