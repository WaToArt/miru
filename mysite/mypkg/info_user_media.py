
class info:
    def __init__(self, id:int=None):
        self.id_primary = id
        self.database = None        
        
        self.type_media:str = None # i.e. Anime, Manga, Light novel
        
        # Will be used create URL links
        ## Options: "anime" and "manga"
        ### IMPORTANT INFO: Light novels are put under the "manga" category, which the url also contains "url"
        self.url_type:str = None 
        
        self.title:str = None

        self.link_mal:str = None 
        self.link_kitsu:str = None
        self.link_anilist:str = None
        
        self.id_mal:int = None # Using "None" works when variable is set as "int" data type.



    # === Batch commands ===
    
    def set_all_links_anime(self):
        # TODO - need to account if series doesn't exist on other websites
        self.set_mal_link()
        # self.set_kitsu_link()
        # self.set_anilist_link()

    def use_database_MAL(self): # MAL database
        
        # TODO - need to account if series doesn't exist on other websites

        # Potential set of sequence depending on which database is the primary one
        self.database = "mal"

    def use_datebase_Anilist(self): # database is Anilist
        # TODO - need to account if series doesn't exist on other websites

        # Potential set of sequence depending on which database is the primary one
        self.database = "anilist"
    def use_datebase_Kitsu(self): # database is Anilist
        # TODO - need to account if series doesn't exist on other websites

        # Potential set of sequence depending on which database is the primary one
        self.database = "kitsu"

    
    # Links will use self.url_types
    # TODO - need to account if webpage doesn't exist on other websites
    def set_mal_link(self):
        new_mal_link = ""
        if self.id_mal == None:
            new_mal_link = "MyAnimeList doesn't have a page :'["
        else:
            new_mal_link = f"https://myanimelist.net/{self.url_type}/{self.id_mal}"
        self.link_mal = new_mal_link
    
    

    def set_kitsu_link(self, kitsu_url:str = None): # FIXME - add parameter where it is a string that contains Kitsu's URL
        new_kitsu_link = ""
        if kitsu_url == None:
            new_kitsu_link = "Kitsu.io doesn't have a page :'("
        else:
            new_kitsu_link = kitsu_url
        self.link_kitsu = new_kitsu_link
        

    def set_anilist_link(self, anilist_url:str =None): #FIXME
        results = ""
        if anilist_url == None:
            results = "Anilist doesn't have a webpage ;["
        else:
            results = anilist_url
        self.link_anilist = results

    # === Scan databases
    
    def scan_database(self):

        pass #TODO - Potentially scan for ids.



class anime(info):
    def __init__(self, id:int):
        super().__init__(id)
        self.type_media = "anime"
        self.url_type:str = "anime"


class manga(info):
    def __init__(self, id:int):
        super().__init__(id)
        self.type_media:str = "Manga"
        self.url_type:str = "manga"


class lightnovel(info):
    def __init__(self, id:int):
        super().__init__(id)
        self.type_media:str = "Light Novel"
        self.url_type:str = "manga"
