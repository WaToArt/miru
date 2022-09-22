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

