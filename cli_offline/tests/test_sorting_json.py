from src.sorting_json import sorting_json

import os
import json

def test_sorted():
    answer_file_name:str = 'sample_expectations.json'
    directories:list[str] = [
        '/database_project_manami/testing_json/',
        './database_project_manami/testing_json',
        '../database_project_manami/testing_json'
    ]

    pathway_of_answer:str = ""
    for directory in directories:
        for root, dirs, files, in os.walk(directory):
            print(root)
            print(dirs)
            print(files)
            if answer_file_name in files:
                pathway_of_answer = os.path.join(root, answer_file_name)
    print(f"Pathway of answer file: {pathway_of_answer}")
    assert pathway_of_answer != ""

    with open(pathway_of_answer) as answer_file:
        json_answer = json.load(answer_file)
    print(json_answer)

    s = sorting_json()


    assert "Finish writing your test!" == "you got this :3"