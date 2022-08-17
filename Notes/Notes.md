
# Abstract:
- Show user a random manga/anime to watch based on the XML from Kitsu.io

- Langauges used:
    - Python
        - Django (backend)
    - PostgreSQL
    - JavaScript
        - Node.js

- App should work locally first...
    - THEN, create a web app using Django (Python) as backend for now.

- Once backend works as visioned, learn how one of the Frontends.
    - Potential front-end options:
        - Node.js
# Primary Objectives:
- Focus on XML from Kitsu.io
   ~~ - Specifically, "Manga" section for now.~~
   - Shifted priority to "Anime" section now.

- # Part 1: Split random manga first

    # Part 2: Spit out random manga to read BASED on "activity status" category selected:
        - Plan to read
        - In progress
        - Done
        - Re-reading

# Bonus objectives:
THIS IS AFTER FINISHING THE PRIMARY OBJECTIVES.

- The second category option: Genre
    - Only issue to that the current kitsu.io's XML doesn't provide this.
    - This might be require active internet activity, and potentially scrap information about genres directly from Kitsu.
    - If possible, maybe see if Kitsu.io has an API to grab some data
        - i.e. Genres 
        - API links:
            - Manga:
                - https://kitsu.docs.apiary.io/#reference/manga
            - Categories:
                - https://kitsu.docs.apiary.io/#reference/categories/categories

# Learning Goals:
- Understand how XML GENERALLY works

- How to use Python and XML together.
    - Add on PostgreSQL and how that could LOCALLY work.

- Learn how JSON works

# How to make "requirements.txt" for pre-reqs: 
- https://stackoverflow.com/a/41458329

# XML Information:
- Manipulating XML with Python:
    - https://www.guru99.com/manipulating-xml-with-python.html

# Lambda expressions:
> Potentially use Lambda expression to filter by reading status, genre, etc.
- guru99: https://www.guru99.com/python-lambda-function.html

# How to read files in Python:
- MOOC.fi: https://programming-22.mooc.fi/part-6/1-reading-files
- Files are need to be in root directory of project.

    - Personal notes: When reading files, account that all file execution will be running from the root directory.
    

- Example of a directory structure: <!-- Refer to this link: https://docs.python.org/3/tutorial/modules.html#packages -->

    - project-rng-manga/ <!-- this is root of project; some files are not included as they are in ".gitignore" -->
        - Docker-compose.yml
        - Dockerfile.dockerfile
        - requirements.txt
        - databases/
            - anime-offline-database.json
        - mysite/
            - manage.py
            - pytest.ini
            - mypkg/
                - __init__.py
                - logic.py
                - media.py
                - ui.py
            - mysite/
                - __init__.py
                - asgi.py
                - settings.py
                - urls.py
                - wsgi.py
            - scans/
                - __init__.py
                - scan_files.py
            - tests/
                - __init__.py
                - conftest.py
                - test_logic.py
                - test_media.py
                - test_scan_files.py
                - test_ui.py
        - Notes/
            - 0-checklists.md
            - apis.md
            - db_info.md
            - info_kitsuio_xml.md
            - links_resources.md
            - notes_anime-offline.database.md
            - Notes_Dockerfile.md
            - Notes.md
            - xml_info.md
        - rng-venv/ <!-- Python's VENV [virtual environment] -->
        - xml-files/ <!-- -->
            - xml_kitsuio/
                - kitsu--anime.xml
                - kitsu--manga.xml
            - xml_mal/
                - animelist_1659156396_-_9830802.xml
                - animelist_1659156396_-_9830802.xml.gz
                - mangalist_1659156419_-_9830802.xml
                - mangalist_1659156419_-_9830802.xml.gz

# *** placeholder ***