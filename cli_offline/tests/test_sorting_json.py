from src.sorting_json import sorting_json

import os
import json

def test_sorted():
    file_name_original:str = 'sample_orignal.json'
    file_name_answer:str = 'sample_expectations.json'
    directories:list[str] = [
        '/database_project_manami/testing_json/',
        './database_project_manami/testing_json',
        '../database_project_manami/testing_json'
    ]

    pathway_of_original:str = ''
    pathway_of_answer:str = ''
    for directory in directories:
        for root, dirs, files, in os.walk(directory):
            print(root)
            print(dirs)
            print(files)

            if file_name_original in files:
                pathway_of_original = os.path.join(root, file_name_original)
            if file_name_answer in files:
                pathway_of_answer = os.path.join(root, file_name_answer)
    print(f"Pathway of oringal file: {pathway_of_original}")
    print(f"Pathway of answer file: {pathway_of_answer}")
    assert pathway_of_original != ''
    assert pathway_of_answer != ''

    with open(pathway_of_original) as original_file:
        json_orignal = json.load(original_file)

    with open(pathway_of_answer) as answer_file:
        json_answer = json.load(answer_file)


    s = sorting_json()
    output_json = s.sort_by_MAL_url(json_orignal)

    assert output_json == json_answer
    assert "Finish writing your test!" == "you got this :3"