import pytest
import random

from scans.scan_json import scan_json

class Test_Scan_Json:
    def setup_class_offline_db(self):
        output_class:scan_json = scan_json()
        output_class.run_db_offline()

        return output_class
    
    def test_random_title(self):
        foo_offline_1 = self.setup_class_offline_db()
        foo_offline_1.set_any_random_title(0)
        output = foo_offline_1.grab_title()

        assert output == '!NVADE SHOW!'


# def setup_scan_json(mocker):
#     output_setup_scan_json = scan_json()
#     mocker.patch('builtins.input', side_effect=[''])
#     output_setup_scan_json.initialize_database()
#     return output_setup_scan_json

# pre_setup_scan_json:scan_json = setup_scan_json()

# def test_variable_pre_setup_scan_json():
#     assert pre_setup_scan_json.online_status == False


    def test_ask_online_status(self):
        scan_json_1 = scan_json()
        output_1 = scan_json_1.online_status
        assert output_1 == False, "Default status should be False. Reason: So it doesn't consume the user's internet data."

        scan_json_1.ask_online_status("no")
        output_2 = scan_json_1.online_status
        assert output_2 == False, "Status should be False now."

        scan_json_1.ask_online_status("yes")
        output_3 = scan_json_1.online_status
        assert output_3 == True, "Status should be True now."

    def test_read_local_db_regular_json_and_verify_passed(self):
        scan_json_2_1 = scan_json()
        scan_json_2_1.read_local_db_regular_json()
        output = scan_json_2_1.verify_repo()
        
        assert output == True, 'Repo should be from "https://github.com/manami-project/anime-offline-database"'

    def test_read_local_db_minified_json_and_verify_passed(self):
        scan_json_2_2 = scan_json()
        scan_json_2_2.read_local_db_minified_json()
        output = scan_json_2_2.verify_repo()
        
        assert output == True, 'Repo should be from "https://github.com/manami-project/anime-offline-database"'

    def test_read_online_db_json_regular_and_verify_passed(self): #Test works, but temporarily disable test as it grabs JSON online
        scan_json_3_0 = scan_json()
        scan_json_3_0.read_online_db_json_regular()
        output = scan_json_3_0.verify_repo()
        
        assert output == True, 'Repo should be from "https://github.com/manami-project/anime-offline-database"'

    def test_read_online_db_json_minified_and_verify_passed(self): #Test works, but temporarily disable test as it grabs JSON online
        scan_json_3_1 = scan_json()
        scan_json_3_1.read_online_db_json_minified()
        output = scan_json_3_1.verify_repo()
        
        assert output == True, 'Repo should be from "https://github.com/manami-project/anime-offline-database"'

    def test_check_mal_id_in_db__regular_json(self,mocker,anime_wotaku_link_mal, anime_wotaku_title): # Testing only
        scan_json_4 = scan_json()
        scan_json_4.initialize_database()
        # output_db = scan_json_4.set_current_anime_from_db(anime_wotaku_link_mal)
        scan_json_4.set_current_anime_from_db(anime_wotaku_link_mal)
        output_db = scan_json_4.current_anime
        
        assert output_db != None, "The MAL link for Wotakoi exists in the anime database from the Manami-Project."
        output_title = scan_json_4.grab_title()
        assert output_title == anime_wotaku_title


    def test_check_mal_id_in_db__minified_json(self, anime_wotaku_link_mal, anime_wotaku_title): # Testing only
        scan_json_4 = scan_json()
        scan_json_4.initialize_database()
        # scan_json_4.read_online_db_json_minified()
        # # output = scan_json_4.check_mal_id_in_db(anime_wotaku_link_mal)
        scan_json_4.set_current_anime_from_db(anime_wotaku_link_mal)

        output_db = scan_json_4.current_anime
        assert output_db != None, "The MAL link for Wotakoi exists in the anime database from the Manami-Project."

        output_title = scan_json_4.grab_title()
        assert output_title == anime_wotaku_title, "Function should return anime information, which contains the title and other information."

    def test_obtain_anime_sources(self, anime_wotaku_link_mal, anime_wotaku_link_anilist, anime_wotaku_link_kitsu):
        scan_json_5 = scan_json()
        scan_json_5.initialize_database()
        scan_json_5.set_current_anime_from_db('https://myanimelist.net/anime/35968')
        # scan_json_5.read_local_db_json()
        # scan_json_5.set_db_all_anime_data()


        dict_sources:dict = scan_json_5.obtain_anime_all_sources() 

        output_mal = dict_sources["mal"]
        output_anilist = dict_sources["anilist"]
        output_kitsu = dict_sources["kitsu"]

        assert output_mal == anime_wotaku_link_mal
        assert output_anilist == anime_wotaku_link_anilist
        assert output_kitsu == anime_wotaku_link_kitsu
        
    def test_failed_obtain_anime_all_sources(self, anime_wotaku_link_mal):
        scan_json_6 = scan_json()
        scan_json_6.initialize_database()

        ## If instance var 'self.current_anime' was None since it func below didn't run
        # scan_json_6.set_current_anime_from_db(anime_wotaku_link_mal)

        dict_sources:dict = scan_json_6.obtain_anime_all_sources() 

        assert dict_sources == None

    def test_grab_title(self, anime_wotaku_link_mal,anime_wotaku_title):
        scan_json_7 = scan_json()
        scan_json_7.initialize_database()
        # scan_json_7.read_local_db_json()
        scan_json_7.set_current_anime_from_db(anime_wotaku_link_mal)

        # output_title = scan_json_7.grab_title(db_anime)
        output_title = scan_json_7.grab_title()

        assert output_title == anime_wotaku_title


    def test_set_any_random_title(self):
        
        
        scan_json_8 = scan_json()
        scan_json_8.initialize_database()
        scan_json_8.set_any_random_title(0)
        output_random_title_1:str = scan_json_8.grab_title()
        assert output_random_title_1 == '!NVADE SHOW!'

        scan_json_8.set_any_random_title(2)
        output_random_title_2:str = scan_json_8.grab_title()
        assert output_random_title_2 == "\"Aesop\" no Ohanashi yori: Ushi to Kaeru, Yokubatta Inu"



