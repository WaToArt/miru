# Background
- v2 of the app to write the code from scratch.
- v1 is messy AND rewriting everything would take a while.
    - It did provide a nice testing ground to learn though.

# Objectives
- Write cleaner code with new knowledge.
    - New knowledge learned from:
        - CS50w
        - Obey the Testing Goat
    - TDD the heck out of the process.
        - Create function tests first, then unit tests.
    - Implement techinques from Obey the Testing Goat.
    - Use match/ switch case if there are a lot of "if/else if" statements!
    - Be strict with type hints and use library mypy
- Create an executable CLI (Command Line Interface) first.
    - This requires less step for users to run the program.
    - Instead of overthinking and taking a while to create a proper webpage, a CLI should be the first step.
        - Follow how the OpenCore Legacy Patcher handles its CLI.
    - Use Pyinstaller to create the exectuables.
- Structure of modules:
    - ui.py
        - ui (user interface) 
    - parse_data.py
        - Consist of two scan classes that searches for info
    - database.py
        - Stores info obtained from parsed info
            - Debatable whether this is needed, but shall see.
- Obtain information directly from Json directly instead of storing all of the json in a global variable.
- Libraries to consider for program:
    - pytest-monitor
        - ~~ Just downloaded (9/22/2022), but need to verify if this checks performance and resource usage as I envisioned.~~
            - Doesn't work on Apple Silicon :'(
    - tkinter
        - Setting up a GUI
            > https://docs.python.org/3/library/tkinter.html
            > https://stackoverflow.com/a/47068925
    - Pyinstaller
        > https://pyinstaller.org/en/stable/
    - pytest-socket
        - I think it forces selected test to run without a network connection
        > https://github.com/miketheman/pytest-socket
    - Progress bar libraries:
        - progressbar2
            >> https://pypi.org/project/progressbar2/
        - tqdm
            >> https://github.com/tqdm/tqdm
            - examples:
                >> https://stackoverflow.com/a/37573701
                >> https://github.com/tqdm/tqdm/blob/master/examples/tqdm_requests.py
            - Used this one:
                >> https://stackoverflow.com/a/56633292
- ***IMPORTANT*** : Implement binary search to quickly grab anime info.
    - Reason: It works best with large set of data.
        - Binary search works with "anime-offline-database.json" as it is:
            - 1-dimension
            - All of the data is sorted
    - Lectures/ examples:
        - https://dev.to/agusioma/big-o-notation-using-python-2ena
        - https://runestone.academy/ns/books/published/pythonds3/SortSearch/TheBinarySearch.html
        - https://cs50.harvard.edu/x/2022/shorts/binary_search/
        - https://towardsdatascience.com/top-algorithms-and-data-structures-you-really-need-to-know-ab9a2a91c7b5

- ***IMPORTANT*** Sorting all data by substring from MAL's url
    - Sorting by substring:
        - https://stackoverflow.com/a/16150890