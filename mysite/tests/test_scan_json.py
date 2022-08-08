import pytest

from scans.scan_json import scan_json

def test_check_online_status():
    scan_json_1 = scan_json()
    output_1 = scan_json_1.online_status
    assert output_1 == True, "Default status should be True."

    scan_json_1.check_online_status("no")
    output_2 = scan_json_1.online_status
    assert output_2 == False, "Status should be False now."

    scan_json_1.check_online_status("yes")
    output_3 = scan_json_1.online_status
    assert output_3 == True, "Status should be True now."

def test_read_local_db_json_and_verify_passed():
    scan_json_2 = scan_json()
    scan_json_2.read_local_db_json()
    output = scan_json_2.verify_repo()
    
    assert output == True, 'Repo should be from "https://github.com/manami-project/anime-offline-database"'

# def test_read_online_db_json_and_verify_passed(): #Test works, but temporarily disable test as it grabs JSON online
#     scan_json_3 = scan_json()
#     scan_json_3.read_online_db_json()
#     output = scan_json_3.verify_repo()
    
#     assert output == True, 'Repo should be from "https://github.com/manami-project/anime-offline-database"'

def test_check_mal_id_in_db(anime_wotaku_link_mal, anime_wotaku_title): # Testing only
    scan_json_4 = scan_json()
    scan_json_4.read_local_db_json()
    # output = scan_json_4.check_mal_id_in_db(anime_wotaku_link_mal)
    output_db = scan_json_4.get_anime_db(anime_wotaku_link_mal)
    assert output_db != None, "The MAL link for Wotakoi exists in the anime database from the Manami-Project."

    output_title = output_db["title"]
    assert output_title == anime_wotaku_title, "Function should return anime information, which contains the title and other information."

def test_obtain_anime_sources(anime_wotaku_link_mal, anime_wotaku_link_anilist, anime_wotaku_link_kitsu):
    scan_json_5 = scan_json()
    scan_json_5.read_local_db_json()


    dict_sources:dict = scan_json_5.obtain_anime_all_sources("https://myanimelist.net/anime/35968") 

    output_mal = dict_sources["mal"]
    output_anilist = dict_sources["anilist"]
    output_kitsu = dict_sources["kitsu"]

    assert output_mal == anime_wotaku_link_mal
    assert output_anilist == anime_wotaku_link_anilist
    assert output_kitsu == anime_wotaku_link_kitsu
    
def test_failed_obtain_anime_all_sources(anime_wotaku_link_mal):
    scan_json_6 = scan_json()
    scan_json_6.read_local_db_json()
    db_anime = scan_json_6.get_anime_db(anime_wotaku_link_mal)

    dict_sources:dict = scan_json_6.obtain_anime_all_sources("https://myanimelist.net/anime/FAILED") 

    assert dict_sources == None

def test_grab_title(anime_wotaku_link_mal,anime_wotaku_title):
    scan_json_7 = scan_json()
    scan_json_7.read_local_db_json()
    db_anime = scan_json_7.get_anime_db(anime_wotaku_link_mal)

    output_title = scan_json_7.grab_title(db_anime)

    assert output_title == anime_wotaku_title