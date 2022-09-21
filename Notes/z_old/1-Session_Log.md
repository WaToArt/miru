# 8/14/2022
- Refactored A LOT of stuff
- Adjusted both module "scan_json.py" and "scan_xml.py" searched for their required local files.
     - Added two potential points to look for the directories.

*** next session ***
- For both scanning modules, readjust that they take the most recent file that was added OR modified.
    - This assumes that the newest file will have the most up to date information.

# 8/9/2022
- Refactored module: info_user_media.py
    - Removed unnecessary instance variables "id" related to Anilist and Kitsu as this was needed.
        - Both sites use MAL are for ids
        - Efficient way is to string URLs of the respective sites instead.
    - Readjusted tests to properly reflect this.
    



# 8/5/2022
- Learned that Anilist also uses MAL's id as their foundation...
    - Need to readjust/cleanup module "info_user_media.py"
- Json
    > Module location: scan_json.py 
        - class scan_json
    - Setup functionality to grabbed links from various sites using substrings of the website's links
        - Function: "grab_link_with_substring()"
        - Setup functionality to grab links of MAL, Anilist, and Kitsu
            - Function: "obtain_anime_all_sources()"
    - Repurposed a function to return the data of an anime
        - Function: "get_anime_db()"
    - renamed various variables and functions for clarity
    *** Next Session: ***
    - Implement the logic to pass information from module "scan_json.py" to "info_db_media.py".
    - Might shift a day to work through CS50w (Web Development), MDN, TOP, and other Full-stack Web Development lessons as a change of pace. The learning day will contribute to this project for the backend (Django) and to learn Front-end.

# 8/4/2022
- JSON
    > Module location: scan_json.py 
        - class scan_json
    - Set up reading JSON for both online and offline context.
        - Function (offline): "read_local_db_json()"
        - Function (online): "read_online_db_json()"

    - Also setup a verification check to make sure that the JSONs came from "https://github.com/manami-project/anime-offline-database"
        - Function: "verify_repo()"


# 8/1/2022
- XML
    - Filtered by ID
        - returns ONLY the MAL-series-ID
    - IP: working on grabbing "my_status"
        - Might need to create separate that that stores ID and status...
            - Might not be efficient speed wise
        - If possible, figure out how to ALSO grab 
- Downloaded updated-Kitsu's XML to include all "my-status"
- created new module "info_db.py" and class "id_info" to store values obtained from kitsu's xml (filename: "kitsu--anime.xml")

# 7/31/2022
- Learn a bit of parsing XML
- pytest.fixtures
    - Added more flags to display info when running Docker compose
- Reliabily setup "open files" so it will always work.
    - Adjust how to copy file by making the folder of the same name and copying files from source to docker's location.
