# Background
- v2 of the app to write the code from scratch.
- v1 is messy AND rewriting everything would take a while.
    - It did provide a nice testing ground to learn though.

# Objectives
- Write cleaner code with new knowledge.
    - TDD the heck out of the process.
        - Create function tests first, then unit tests.
    - Implement techinques from Obey the Testing Goat.
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