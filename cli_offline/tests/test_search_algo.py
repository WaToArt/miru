from src.search_algo import Search_algo

def test_binary_search_recursion():
    list_values:list[str] = [
    "Adam", 
    "beef", 
    "colobunga", 
    "dude", 
    "eric", 
    "frieza",
    "goku drip",
    ]

    s:Search_algo = Search_algo()
    target_string:str = list_values[4]
    start:int = 0
    end:int = len(list_values) - 1
    result:int = s.binary_search_recursion(list_values, target_string)

    assert result == 'eric'

def test_binary_search_looping():
    list_values:list[str] = [
    "Adam", 
    "beef", 
    "colobunga", 
    "dude", 
    "eric", 
    "frieza",
    "goku drip",
    ]

    s:Search_algo = Search_algo()
    target_string:str = list_values[4]
    result:int = s.binary_search_looping(list_values, target_string)

    assert result == 4

    