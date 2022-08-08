import sys
from xml.etree import ElementTree as ET
from random import sample, choice
from mypkg.info_db_media import db_info

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

    def __init__(self, file_name:str, website:str, format_media:str) -> None:
        self.root = self.parse_xml(file_name)
        self.website = website.lower()
        self.syntax_id = None
        self.syntax_my_status = None
        self.format_media = None

        # Run functions ASAP
        self.set_format_database()
        self.set_format_media(format_media.lower())


    # RSRC 2
    def parse_xml(self, file_name):
        try:
            tree = ET.parse(file_name) # These commands negate the need for "with open"
            root = tree.getroot()
            return root
        except FileNotFoundError as E:
            print(f"Error: {E}")
            print("Ending program now.")
            sys.exit()
    def set_format_media(self, format_media):
        m_formats:list = ["anime","manga","light novel"]
        if format_media in m_formats:
            self.format_media = format_media
            
    def set_format_database(self):
        if self.website == "anilist":
            self.syntax_id = None
            self.syntax_my_status = None # TEMPORARY
        elif self.website == "myanimelist" or self.website == "kitsu": # Default to MAL, which MAL and Kitsu uses
            # self.syntax_id = "series_animedb_id"
            self.syntax_id = "series_animedb_id" # use "return" instead of reassigning new string IF the function is immediately being called in __init__.py
            self.syntax_my_status = "my_status"
        else:
            self.syntax_id = None
            self.syntax_my_status = None
    def check_ids_all_status(self, id_db:str = None): # Foundation/ Example of how to check for id.
        # RSRC 4
        if id_db == None:
            id_db = self.syntax_id
        
        output_list = []

        # Main loop
        for values in self.root.iter(id_db):
            if values not in output_list:
                output_list.append(int(values.text))
        
        return output_list
    
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
            
            output_list.append(db_info(id_media, my_status,self.format_media))

        return output_list
        
    # RSRC 3
    def get_random_id(self, option_arg1:list = None): # Maybe move to different module later
        if option_arg1 == None:
            return choice(self.check_ids_all_status())
        else:
            return choice(option_arg1)

    def check_my_status(self):
        pass


    





if __name__ == '__main__':
    file_kitsu_anime = "./xml_files/xml_kitsuio/kitsu--anime.xml"

    scan_class = scan_xml(file_kitsu_anime, "kitsu")
    output = scan_class.check_anime_name()



    print(output)
    print("\n ====== \n")


