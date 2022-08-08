import requests
import json



class scan_json:
    def __init__(self) -> None:
        self.online_status:bool = True #True or False if to check database online. 
        self.json_data = None
        self.correct_repo_url:str = "https://github.com/manami-project/anime-offline-database"
    
    def start_program(self) -> None:
        # Order to run function
            # check_online_status; either go online or stay offline

        
        output = None #TODO



        return output


    def check_online_status(self, input_command:str) -> None:
        accepted_answers:list = ['yes','no']
        user_command = input_command.strip().lower()
        
            
        if user_command == "yes":
            self.online_status = True
        elif user_command == "no":
            self.online_status = False
        else: 
            print('Try again. Input "yes" or "no".')

    
    def read_local_db_json(self): # RSRC 6 | 
        # TODO - figure out how to use open and read JSON file
        db_file_path = "./databases/anime-offline-database.json"
        # add a catch to whether the file existed or not 
        
        data = None
        try:
            with open(db_file_path,'r') as db_offline_anime:
                data_offline = json.load(db_offline_anime) #Swapped from "json.loads()" to "json.load()", which stopped triggering this erroe: "TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper". json.loads couldn't read a TextIOWrapper format

                # return data_offline
                self.json_data = data_offline
        except FileNotFoundError as e:
            print(f"Error: {e}")
        


    
    def read_online_db_json(self) -> json: 
        
        # Anime database JSON is from https://github.com/manami-project/
        url = 'https://github.com/manami-project/anime-offline-database/blob/master/anime-offline-database.json?raw=true'

        # RSRC 5
        resp = requests.get(url)
        data_online = json.loads(resp.text) 

        self.json_data = data_online

    
    def verify_repo(self) -> bool:
        verification:bool = False

        # add code to scan for data info with self.correct_repo_url
        current_db_url = self.json_data["repository"]
        if current_db_url == self.correct_repo_url:
            verification = True

        return verification
    
    def get_anime_db(self, url_anime:str) -> str: #FIXME - possibly repurpose this to be more general to work for anilist and Kitsu as well?
        output = None

        db_all_anime = self.json_data["data"]

        for title in db_all_anime:
            sources = title["sources"]
            if url_anime in sources:
                output = title
                break

        return output
    
    def obtain_anime_all_sources(self, url_anime:str):
        # Contains links for MAL, Anilist, and Kitsu
        links_substrings:list = ["https://myanimelist.net/anime/", 
            "https://anilist.co/anime/", 
            "https://kitsu.io/anime/"]

        db_anime_info = self.get_anime_db(url_anime)
        # if link was not found in database, return result None immediately
        if db_anime_info == None:
            return None

        output_sources:dict = {"mal": None, "anilist": None, "kitsu": None} # RSRC 8 - Using dict over list as it seems to be faster to grab
        output_sources["mal"] = self.grab_link_with_substring(db_anime_info,links_substrings[0])
        output_sources["anilist"] = self.grab_link_with_substring(db_anime_info,links_substrings[1])
        output_sources["kitsu"] = self.grab_link_with_substring(db_anime_info,links_substrings[2])

        # TODO - Figure out logic to use substrings to grab the full string (containing ID)
        
        return output_sources

    def grab_link_with_substring(self, db_anime, substring_url:str):
        # RSRC 9 && RSRC 10
        ouput_full_string = next(full_string for full_string in db_anime["sources"] if substring_url in full_string)

        return ouput_full_string
    
    def grab_title(self, db_anime):
        return db_anime["title"]
        
if __name__ == "__main__":
    test = scan_json()
    test.read_local_db_json()
    output = test.get_anime_db("myanimelist.net/anime/35968")
    print(type(output)) # This works fine