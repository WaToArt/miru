from parse_anime_db import download_anime_database_json

def main():
    download_db:download_anime_database_json = download_anime_database_json()
    anime_json:dict = download_db.download_json()
    repo = anime_json["repository"]
    first_anime_entry = anime_json["data"][0]

    print(first_anime_entry)

if __name__ == "__main__":
    main()