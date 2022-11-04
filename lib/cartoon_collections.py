def roll_call_dwarves(list):
    for index, dwarf in enumerate(list):
        print(f'{index+1}. {dwarf}')
    pass

def summon_captain_planet(arr):
    result = map(change,arr)
    return  list(result)

def long_planeteer_calls(arr):
    result = map(check_length, arr)
    return any(list(result))
    

def find_the_cheese(arr):
    cheeses = ["cheddar", "gouda", "camembert"]
    for el in arr:
        if el in cheeses:
            return el
    return None
    

def change(str):
    x= str[0].capitalize()
    return x + str[1:len(str)] + "!"

def check_length(x):
    return len(x) > 4
