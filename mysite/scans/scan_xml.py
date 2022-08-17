import os
import sys
from xml.etree import ElementTree as ET
from random import sample, choice
from datetime import date


# from ..mypkg.info_db_media import db_info

class read_file:
    def __init__(self):
        self.file_name:str = "file_name"
    
    # How to read files: https://programming-22.mooc.fi/part-6/1-reading-files
    ## This is a reference/example.
    def output_FileNotFound(self, E):
        return (f"sadge ੨( ･᷄ ︵･᷅ )ｼ. Error: {E}")

    def readline_file(self, file_name:str):
        file_name:str = file_name
        try:    
            data = None
            with open(file_name,'r') as file_imported:
                data = file_imported.readline().replace('\n',"")
            
            return data
        except FileNotFoundError as E:
            print("")
            return self.output_FileNotFound(E).replace('\n', "")


class scan_xml:

    def __init__(self, format_media:str, website:str = 'mal') -> None:
        self.format_media = None
        self.website = website.lower()
        self.root = None
        # self.root = self.parse_xml(file_name)

        self.syntax_id = None
        self.syntax_my_status = None
        self.list_users_all_anime_data: list = None
        
        # Run functions ASAP
        self.parse_xml()
        self.set_format_anime_database()
        self.set_format_media(format_media.lower())
        self.check_animeid_MAL()

    # RSRC 2
    def parse_xml(self, file_name:str = None):
        if file_name == None:
            file_name = self.search_xml_location()

        try:
            tree = ET.parse(file_name) # These commands negate the need for "with open"
            self.root = tree.getroot()
            # root = tree.getroot()
            # return root
        except FileNotFoundError as E:
            print(f"Error: {E}")
            print("Ending program now.")
            sys.exit()

    # RSRC 12
    def search_xml_location(self) -> str: # TODO
        website_locations:dict = {
            'mal': ['./xml_files/xml_mal', 
            '../xml_files/xml_mal'],

            'anilist': ['./xml_files/xml_anilist',
            '../xml_files/xml_anilist'],

            'kitsu': ['./xml_files/xml_kitsuio',
            '../xml_files/xml_kitsuio']
        }
        website_substrings:dict = {
            'mal': ['animelist_', 
            ],
            
            'anilist': ['scrape_anilistanimealt', 
            ],
            
            'kitsu': ['kitsu--anime', 
            ],
        }

        chosen_site_substring:list[str] = website_substrings.get(self.website)
        chosen_site_locations:list[str] = website_locations.get(self.website)

        for location in chosen_site_locations:
            for root, dirs, files, in os.walk(location):
                for file in files:
                    for substring in chosen_site_substring:
                    # if chosen_site_substring in file and file.endswith('.xml'):
                    #     regular_json_location = os.path.join(root,file)
                    #     return regular_json_location
                        if substring in file and file.endswith('.xml'):
                            regular_json_location = os.path.join(root,file)
                            return regular_json_location

    def set_format_media(self, format_media:str):
        m_formats:list = ["anime","manga","light novel"]
        if format_media in m_formats:
            self.format_media = format_media
            
    def set_format_anime_database(self):
        # MAL, Anilist, and Kitsu all use MAL's id as the foundation.
        self.syntax_id = "series_animedb_id" # use "return" instead of reassigning new string IF the function is immediately being called in __init__.py
        self.syntax_my_status = "my_status"
    
    def set_format_manga_database(self):
        pass
    
    def set_format_light_novels_database(self):
        pass

    # def check_ids_all_status(self, id_db:str = None): # Foundation/ Example of how to check for id.
        
    #     output_list = []

    #     # Main loop # RSRC 4
    #     for values in self.root.iter(self.syntax_id):
    #         if values not in output_list:
    #             output_list.append(int(values.text))
        
    #     return output_list
    
    # This works for MAL database
    def check_animeid_MAL(self): # TODO - change to findall and use find while in for loop
        # Psuedocode | Parent and children:
            #anime
                #series_animedb_id
                #my_status
        
        output_list:list = []
        for entry in self.root.findall("anime"):

            id_media:int = int(entry.find(self.syntax_id).text) #TODO 
            my_status:str = entry.find(self.syntax_my_status).text #TODO
            my_watch_episodes:int = int(entry.find("my_watched_episodes").text)
            
            start_date = "Haven't started yet :'["
            if "my_start_date" in entry:
                start_date = date.fromisoformat(entry.find("my_start_date").text)
            
            finish_date = "Haven't finished yet :'("
            if "my_finish_date" in entry:
                finish_date = date.fromisoformat(entry.find("my_finish_date").text)

            my_times_watched:int = int(entry.find("my_times_watched").text)

            output_list.append([id_media,my_status, my_watch_episodes, start_date, finish_date, my_times_watched])
        # return output_list
        self.list_users_all_anime_data = output_list
    
    def get_list_ids(self):
        output_list:list = []
        for title in self.list_users_all_anime_data:
            output_list.append(title[0])
        
        return output_list
        
    # # RSRC 3
    # def get_random_id_v1(self, optional_int:int = None) -> int: # Maybe move to different module later
    #     if optional_int == None:
    #         return choice(self.get_list_ids())
    #     else:
    #         return (self.get_list_ids)[optional_int]
    
    def get_random_id_v2(self, optional_int:int = None) -> int: # Maybe move to different module later
        if optional_int == None:
            output_chosen:list = choice(self.list_users_all_anime_data)
            return output_chosen[0]
        else:
            return (self.get_list_ids)[optional_int]
        
    def get_random_title_info(self, optional_int:int = None)  -> list:
        if optional_int == None:
            return choice(self.list_users_all_anime_data)
        else:
            return self.list_users_all_anime_data[optional_int]
        # TODO


    def check_my_status(self):
        pass

class MAL_anime_xml(scan_xml):
    def __init__(self, format_media: str, website: str = 'mal') -> None:
        super().__init__(format_media, website)

class Anilist_anime_xml(scan_xml):
    def __init__(self, format_media: str, website: str = 'anilist') -> None:
        super().__init__(format_media, website)

class Kitsu_anime_xml(scan_xml):
    def __init__(self, format_media: str, website: str = 'kitsu') -> None:
        super().__init__(format_media, website)






### === DEBUGGING ZONE === ###
# import time, statistics
# def time_testing():
#     file_kitsu_anime = "./xml_files/xml_kitsuio/kitsu--anime.xml"

#     scan_class = scan_xml(file_kitsu_anime, "kitsu", "anime")

#     outer_index = 0
#     v1_victory = 0
#     v2_victory = 0
#     tied = 0
#     while outer_index < 20:
#         print(outer_index)
        
#         index = 0
#         v1_list:list = []
#         v2_list:list = []
#         while index < 1000:
#             print(f'attempt {index}')
#             print('====')
            
#             print("v1 results:")
#             v1_start_time = time.time()
#             print(scan_class.get_random_id_v1())
#             v1_end_time = time.time()
#             v1_total = v1_end_time - v1_start_time
#             print(v1_total)
#             v1_list.append(v1_total)
#             print('=======')

#             print("v2 results:")
#             v2_start_time = time.time()
#             print(scan_class.get_random_id_v2())
#             v2_end_time = time.time()
#             v2_total = v2_end_time - v2_start_time
#             print(v2_total)
#             v2_list.append(v2_total)
            

#             index += 1

#         v1_average = statistics.mean(v1_list)
#         v2_average = statistics.mean(v2_list)

#         difference_averages:int = None
#         faster_average:str = None
#         if v1_average < v2_average:
#             faster_average = 'v1'
#             difference_averages = v2_average - v1_average
#             v1_victory += 1

#         elif v2_average < v1_average:
#             faster_average = 'v2'
#             difference_averages = v1_average - v2_average
#             v2_victory += 2
#         else:
#             faster_average = 'Both are the same'
#             difference_averages = 0
#             tied += 1

#         print('\n\n\n')
#         print(f'Result of time test: {faster_average}. The difference was {difference_averages}')
#         print(f'v1 average: {v1_average}')
#         print(f'v2 average: {v2_average}')
#         outer_index += 1
    

#     print('\n\n\n')
#     print('Final verdict:')
#     if v1_victory > v2_victory:
#         print("v1 is good")
#     elif v2_victory > v1_victory:
#         print("v2 good")
#     else:
#         print("same")
#     print(f"v1 victories: {v1_victory}")
#     print(f"v2 victories: {v2_victory}")
#     print(f'tied: {tied}')


if __name__ == '__main__':
    file_kitsu_anime = "./xml_files/xml_kitsuio/kitsu--anime.xml"

    scan_class = scan_xml(file_kitsu_anime, "kitsu", "anime")

    # print(time_testing())

    print(scan_class.get_random_title_info())
