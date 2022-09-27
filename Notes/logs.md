

# 9/27/2022

- Read this on how to remove files after running tests:
    >> https://stackoverflow.com/a/51593679
    >> https://docs.pytest.org/en/6.2.x/tmpdir.html

# 9/26/2022



- CMD of running functions in action WITH a new json online:

(venv_miru) watoart@Richs-MacBook-Air miru %  /usr/bin/env /Users/watoart/VSCode/miru/venv_miru/bin/python /Users/watoart/.vscode/extensions/ms-python.python-2022.14.0/pythonFiles/lib/python/debugpy/adapter/../../debugpy/laun
cher 54126 -- /Users/watoart/VSCode/miru/cli_offline/src/parse_info.py 
anime-offline-database-minified.json was found. This will be used :3
Sucess! Correct repo :3
There's a newer json online :O
Sucessfully downloaded one of the databases! "anime-offline-database-minified.json" was downloaded and saved locally with the size of (41.765094 mb) :D
done!
(venv_miru) watoart@Richs-MacBook-Air miru %  cd /Users/watoart/VSCode/miru ; /usr/bin/env /Users/watoart/VSCode/miru/venv_miru/bin/python /Users/watoart/.vscode/extensions/ms-python.python-2022.14.0/pythonFiles/lib/python/de
bugpy/adapter/../../debugpy/launcher 54134 -- /Users/watoart/VSCode/miru/cli_offline/src/parse_info.py 
anime-offline-database-minified.json was found. This will be used :3
Sucess! Correct repo :3
The local json is up-to-date :3
Sucessfully downloaded one of the databases! "anime-offline-database-minified.json" was downloaded and saved locally with the size of (41.765094 mb) :D
done!

# 9/25/2022

- ENDING SESH
    - Things completed:
        - functions: 
            - comparing dates
            - correct repo
    - These needs unit tests to be written. Keep focusing too much on writting them to work.

- Important info from json to verify:
    "license": {
        "name": "GNU Affero General Public License v3.0",
        "url": "https://github.com/manami-project/anime-offline-database/blob/master/LICENSE"
    },
    "repository": "https://github.com/manami-project/anime-offline-database",
    "lastUpdate": "2022-09-21",
# 9/24/2022

- Implemented download progress bar with tdqm.
    - Using Stream allows the file to be downloaded in chunks
        - UPDATE: progress bar isn't being updated. No iteration/for loop is actively updating the progress bar

- NExt time:
    - Learn how to validate json
        - Read this:
            > https://stackoverflow.com/a/54491882
            >> https://pypi.org/project/jsonschema/
- Ending sesh:
    - Finished implementating and writing test for function:
        - read_json()
            - There might be scenarios I am unaccounting for.
            - I think it might be to verify the repo before saving locally.
            - Need to implement a check whether the the existing local json  is newer or older.


- Resuming session:
    - ~~Working on download_json() first~~ #Complete
        - Need to add script:
            ~~ > If folder doesn't exist, create the directory to contain the database. ~~ #Completed
        

    

# 9/23/2022

- Next sesh:
    - Work on:
        - read_json()
        - download_json()
        

- Worked on today:
    - class: parsed_anime_database
        - functions:
            - read_json()
            - download_json()

# 9/22/2022

- Next time:
    - Read how to work with JSON
        - Resources to read on topic:
            > https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
            > https://cs50.harvard.edu/web/2018/notes/4
            > https://cs50.harvard.edu/web/2020/notes/5/
        - Potentially examples on how Json is used?:
            > ~~ https://github.com/lagmoellertim/pyon ~~ This is library, so nope.

- Uninstalled pytest-monitor as it doesn't work on Apple Silicon

- Implemented finding pathway of anime database json file.