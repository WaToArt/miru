import os
import requests
import json
import random



class scan_json:
    def __init__(self) -> None:
        self.online_status:bool = False #True or False if to check database online. 
        self.json_data = None
        self.db_all_anime_data = None
        self.correct_repo_url:str = "https://github.com/manami-project/anime-offline-database"

        self.current_anime = None
    

# === Database setup ===
    def run_db_offline(self, file_location:str = None) -> None:
        self.online_status = False
        self.initialize_database(file_location)

    
    def run_db_online(self) -> None:
        self.online_status = True
        self.initialize_database()

    def initialize_database(self, file_location:str = None) -> None: #TODO - do this to save time for tests
        # Order to run function:
            # func 'check_online_status'; either go online or stay offline
                # if status:
                    # ONLINE: run func 'read_online_db_json_minified'
                    # OFFLINE: run func 'read_local_db_minified_json'
            # func 'verify_repo'
                # if false, return that repo didn't match and ask to download proper database OR go online instead
            # func 'set_db_all_anime_data'
        
        # input_online_status:str = ''
        # # while True:
        # #     accepted_answers:list = ['yes','no','']
        # #     input_online_status:str = (input("Do you want to use the online database? If no, we can use the local file.")).lower() #FIXME - repharse this part later.
        # #     if input_online_status in accepted_answers:
        # #         break

        # self.ask_online_status(input_online_status)
        
        if self.online_status == True:
            self.read_online_db_json_minified()
        else:
            self.read_local_db_minified_json(file_location)

        self.verify_repo()
        self.set_db_all_anime_data()

    def ask_online_status(self, input_command:str = '') -> None:
        accepted_answers:list = ['yes',
        'no',
        '',
        ]
        user_command = input_command.strip().lower()
        
        match user_command:
            case "yes":
                self.online_status = True
            case "no":
                self.online_status = False
            case _:
                print(f"Defaulting to No")
                self.online_status = False
        # if user_command == "yes":
        #     self.online_status = True
        # else:
        #     self.online_status = False
        
        ### Revision 1
        # elif user_command == "no" or user_command == '':
        #     self.online_status = False
        # else: 
        #     print('Try again. Input "yes" or "no".')

    
    def read_local_db_regular_json(self, regular_db_file_path:str = None) -> json: # RSRC 6 | 
        if regular_db_file_path == None:
            regular_json_filename = 'anime-offline-database.json'
            regular_db_file_path = self.search_json_location(regular_json_filename)

        try:
            with open(regular_db_file_path,'r') as db_offline_anime:
                data_offline = json.load(db_offline_anime) #Swapped from "json.loads()" to "json.load()", which stopped triggering this erroe: "TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper". json.loads couldn't read a TextIOWrapper format

                self.json_data = data_offline
        except FileNotFoundError as e:
            print(f"Error: {e}")
    
    def read_local_db_minified_json(self, minified_db_file_path:str = None) -> json:
        
        if minified_db_file_path == None:
            minified_json_filename = 'anime-offline-database-minified.json'
            minified_db_file_path = self.search_json_location(minified_json_filename)

        try:
            with open(minified_db_file_path,'r') as db_offline_anime:
                data_offline = json.load(db_offline_anime) #Swapped from "json.loads()" to "json.load()", which stopped triggering this erroe: "TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper". json.loads couldn't read a TextIOWrapper format

                self.json_data = data_offline
        except FileNotFoundError as e:
            print(f"Error: {e}")

    # RSRC 14
    def search_json_location(self, filename:str):
        directories:list[str] = ['./databases/',
        '../databases/',
        ]
        for directory in directories:
            for root,dirs,files, in os.walk(directory):
                for file in files:
                    if filename in file and file.endswith('.json'): # RSRC 15
                        minified_db_file_path = os.path.join(root, file)
                        return minified_db_file_path

        return None

    def read_online_db_json_regular(self) -> json: 
        
        # Anime database JSON is from https://github.com/manami-project/
        url = 'https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database.json?raw=true'

        # RSRC 5
        resp = requests.get(url)
        data_online_regular = json.loads(resp.text) 

        self.json_data = data_online_regular
    
    def read_online_db_json_minified(self) -> json: 
        
        # Anime database JSON is from https://github.com/manami-project/
        url = 'https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database-minified.json?raw=true'

        # RSRC 5
        resp = requests.get(url)
        data_online_minified = json.loads(resp.text) 

        self.json_data = data_online_minified

    def verify_repo(self) -> bool:
        verification:bool = False

        # add code to scan for data info with self.correct_repo_url
        current_db_url = self.json_data["repository"]
        if current_db_url == self.correct_repo_url:
            verification = True

        return verification

    def set_db_all_anime_data(self) -> None:
        self.db_all_anime_data = self.json_data["data"]

        # Empty instance variable 'self.json_data' since the focus is on instance variable 'self.db_all_anime_data' from here on out
        self.json_data = None

# === Obtaining specific anime information ===
    
    def set_current_anime_from_db(self, url_anime:str) -> None: #FIXME - possibly repurpose this to be more general to work for anilist and Kitsu as well?

        for title in self.db_all_anime_data:
            sources = title["sources"]
            if url_anime in sources:
                self.current_anime = title
                return
        
        self.current_anime = None

    def obtain_anime_all_sources(self) -> dict:
        # Contains links for MAL, Anilist, and Kitsu
        links_substrings:list = ["https://myanimelist.net/anime/", 
            "https://anilist.co/anime/", 
            "https://kitsu.io/anime/"]

        # if link was not found in database, return result None immediately
        if self.current_anime == None:
            return None

        output_sources:dict = {"mal": None, "anilist": None, "kitsu": None} # RSRC 8 - Using dict over list as it seems to be faster to grab
        
        output_sources["mal"] = self.grab_link_with_substring(links_substrings[0])
        output_sources["anilist"] = self.grab_link_with_substring(links_substrings[1])
        output_sources["kitsu"] = self.grab_link_with_substring(links_substrings[2])

        # TODO - Figure out logic to use substrings to grab the full string (containing ID)
        
        return output_sources

    def grab_link_with_substring(self, substring_url:str) -> str:
        # RSRC 9 && RSRC 10 && RSRC 13
        output_full_string_url = None

        # ouput_full_string_url = next(full_string for full_string in self.current_anime["sources"] if substring_url in full_string)

        for website in self.current_anime['sources']:
            if substring_url in website:
                output_full_string_url = website
                break

        return output_full_string_url
    
    def grab_title(self) -> str:
        return self.current_anime["title"]

# === Pure randomness ===
    def set_any_random_title(self,random_seed:int = None) -> None:
        # RSRC 11
        if random_seed == None:
            random_seed = random.randrange(len(self.db_all_anime_data))
        self.current_anime = self.db_all_anime_data[random_seed]

if __name__ == "__main__":
    # test = scan_json()
    # test.initialize_database()
    # chosen_anime = test.get_anime_from_db("myanimelist.net/anime/35968")
    # print(chosen_anime)

    # output = test.grab_title(chosen_anime)
    # print(output) # This works fine

    scan_json_7 = scan_json()
    scan_json_7.
    print(output_title)