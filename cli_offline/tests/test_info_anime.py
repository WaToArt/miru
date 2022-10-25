from src.info_anime import anime

class Tests_info_anime:
    def test_stock_information_and_store_wotakoi(self):
        wotakoi_mal_id:int = 35968
        wotakoi_mal_url:str = "https://myanimelist.net/anime/35968"
        wotakoi_anilist:str = "https://anilist.co/anime/99578"
        wotakoi_kitsu:str = "https://kitsu.io/anime/13660"
        
        wotakoi_anime:anime = anime()
        assert wotakoi_anime.mal_id == -1
        assert wotakoi_anime.mal_url == ""
        assert wotakoi_anime.anilist_url == ""
        assert wotakoi_anime.kitsu_url == ""

        wotakoi_anime.mal_id = 35968
        wotakoi_anime.mal_url = "https://myanimelist.net/anime/35968"
        wotakoi_anime.anilist_url = "https://anilist.co/anime/99578"
        wotakoi_anime.kitsu_url = "https://kitsu.io/anime/13660"

        assert wotakoi_anime.mal_id == wotakoi_mal_id
        assert wotakoi_anime.mal_url == wotakoi_mal_url
        assert wotakoi_anime.anilist_url == wotakoi_anilist
        assert wotakoi_anime.kitsu_url == wotakoi_kitsu
    
    