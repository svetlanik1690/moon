import json
INPUT_FILE = 'input.json'


def task(su=0) -> float:
    with open(INPUT_FILE) as f1:
        python_obj = json.load(f1)
        for slovar in python_obj:
            score = slovar['score']
            weight = slovar['weight']
            pr = score * weight
            su += pr
    return su


print(round(task(), ndigits=3))
