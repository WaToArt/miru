from parse_anime_db import download_anime_database_json
from search_algo import Search_algo as s_algo

def main():
    download_db:download_anime_database_json = download_anime_database_json()
    anime_json:dict = download_db.download_json()
    repo = anime_json["repository"]
    wotakoi_mal_url:str = "https://myanimelist.net/anime/35968"

    wotakoi_index_in_database:int = s_algo().sequential_search_fnb_myanimelist_url(anime_json, wotakoi_mal_url)

    print(f"Wotakoi's index in the database: {wotakoi_index_in_database}")
    print(f"Printing all of Wotakoi's database info:")
    print(anime_json["data"][wotakoi_index_in_database])

if __name__ == "__main__":
    main()