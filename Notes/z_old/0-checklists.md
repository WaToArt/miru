# Checklist
- ~~Create Dockerfile~~
    - ~~Potentially Dockercompose too~~
    - ~~un "docker compose up" in directory "/mysite/"~~
- Have both scan modules ('scan_json' and 'scan_xml') grab the latest files.
- Setup logic class so it doesn't need to be setup in the Django apps

- ~~Learn how to scan/use file on Python~~
- ~~Learn how to parse info from XML~~
- ~~Learn how to scan through JSON~~
    - ~~Try to scan for MAL's URL link within "source", which contains the series id.~~
    - Combine the info from module "info_db.py" with the new info from the JSON databse (provided by minami-project)
        - Link the id from kitsu to the JSON database...
            - JSON will provide the id:
                - Title
                - other website's ID
        - Obtain db's "last update" to show users when the db was last updated

-  Current objective *** Setup Django app by outputting completely random title from anime-database ***
    > Implement Django knowledge as this is first time practice.
    - App name:
        - purerandomtitles
    - Output:
        - Obtain random anime title
    - Create func to grab random title.
    - Setup HTML
    - Styling:
        - Center the output
    - When website is deployed, allow user to upload their XML to run the app
- MAYBE...
    - After scanning a file, maybe save it to a local file so program runs again next time, it saves time?
        - Ask user if they want to use an updated-XML file
        - Figure out how an updated file might trigger to scan automatically?
    - Sessions
        >> https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Sessions
        >> https://cs50.harvard.edu/web/2020/notes/3/#sessions
        - Could be used to store each store's session/ data locally? This way, the app still works offline.

> Misc
- Learn how to implement Django
- Learn how to use APIs
- Use APIs from Kitsu
- Use APIs from Anilist
- Use APIs from MyAnimeList (MAL)
- Implementing Switch/Match?
    >> https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/



- Learn Front-end...
    - ~~ HTML~~
    - ~~ CSS~~
    - JavaScript
        - React

