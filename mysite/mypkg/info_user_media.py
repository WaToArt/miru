
class info:
    def __init__(self, id:int):
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
        self.id_kitsu:int = None
        self.id_anilist:int = None


    # === Batch commands ===
    
    def set_all_links(self):
        # TODO - need to account if series doesn't exist on other websites
        self.set_mal_link()
        self.set_kitsu_link()
        self.set_anilist_link()

    def use_database_MAL(self, title, kitsu_id, anilist_id): # MAL database
        
        # TODO - need to account if series doesn't exist on other websites

        # Potential set of sequence depending on which database is the primary one
        self.id_mal = self.id_primary
        self.database = "MAL"

        self.title = title
        self.id_kitsu = kitsu_id
        self.id_anilist = anilist_id

    def use_datebase_Anilist(self, title, mal_id, kitsu_id): # database is Anilist
        # TODO - need to account if series doesn't exist on other websites

        # Potential set of sequence depending on which database is the primary one
        self.id_anilist = self.id_primary
        self.database = "Anilist"

        self.title = title
        self.id_mal = mal_id
        self.id_kitsu = kitsu_id
    
    # Links will use self.url_types
    # TODO - need to account if webpage doesn't exist on other websites
    def set_mal_link(self):
        new_mal_link = ""
        if self.id_mal == None:
            new_mal_link = "MyAnimeList doesn't have a page :'["
        else:
            new_mal_link = f"https://myanimelist.net/{self.url_type}/{self.id_mal}"
        self.link_mal = new_mal_link
    
    

    def set_kitsu_link(self):
        new_kitsu_link = ""
        if self.id_kitsu == None:
            new_kitsu_link = "Kitsu.io doesn't have a page :'("
        else:
            new_kitsu_link = f"https://kitsu.io/{self.url_type}/{self.id_kitsu}"
        self.link_kitsu = new_kitsu_link
        

    def set_anilist_link(self):
        results = ""
        if self.id_anilist == None:
            results = "Anilist doesn't have a webpage ;["
        else:
            results = f"https://anilist.co/{self.url_type}/{self.id_anilist}"
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
