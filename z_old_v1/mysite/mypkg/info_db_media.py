class db_info:
    def __init__(self, id_media:int, my_status:str,format_media:str) -> None:
        self.id_media:int = id_media
        self.my_status:str = my_status
        self.format_media:str = format_media
        
        # Will add more later class variables later

    def __str__(self) -> str:
        return f'{self.id_media} | {self.my_status}'