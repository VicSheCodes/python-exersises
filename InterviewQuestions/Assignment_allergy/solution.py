from typing import List

ALLERGY_SCORES = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}

def is_allergic_to(score: int, allergen: str) -> bool:
    scores_arr = list(ALLERGY_SCORES.values())
    print('allergy scores vlues', scores_arr)
    if score not in scores_arr:
      return False
    n = len(ALLERGY_SCORES)
    list_1 = list() 
    # There are total 2^n subsets
    total = 1 << n
    # Consider all numbers from 0 to 2^n - 1
    for i in range(total):
      Sum = 0
      for j in range(n):
        if ((i & (1 << j)) != 0):
            Sum += scores_arr[j]
      list_1.append(Sum)      
    list_1.remove(0)
    if ALLERGY_SCORES.get(allergen) == score:
        return ALLERGY_SCORES.get(allergen) == score
    if score in list_1:
        return True

    return False

    pass
  
def allergies(score: int) -> List[str]:
        list = []
        for allergy in ALLERGY_SCORES:
            if is_allergic_to(score, allergy):
                list.append(allergy)
        return sorted(list)
pass