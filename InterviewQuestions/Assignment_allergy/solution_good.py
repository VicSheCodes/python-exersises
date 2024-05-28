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
  list = [allergy for (allergy, score2) in ALLERGY_SCORES.items() if score2 & score != 0]

  return allergen in list
  pass
  
def allergies(score: int) -> List[str]:
#  list = []
#  for allergy in ALLERGY_SCORES:
#     if is_allergic_to(score, allergy):
#          list.append(allergy)
  list = [allergy for allergy in ALLERGY_SCORES if is_allergic_to(score, allergy)]
          
  return sorted(list)
  pass