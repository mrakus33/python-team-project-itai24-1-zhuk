import math

def calculate_average(grades: list[float]) -> float:
   if not grades:
      return 0.0
   return sum(grades) / len(grades)

def calculate_min_max(grades: list[float]) -> tuple[float, float]:
   if not grades:
      return 0.0, 0.0
   return min(grades), max(grades)

def calculate_standard_deviation(grades: list[float]) -> float:
   if not grades or len(grades) < 2:
      return 0.0
   avg = calculate_average(grades)
   variance = sum((x - avg) ** 2 for x in grades) / len(grades)
   return math.sqrt(variance)

def sort_students(students_data: list[dict]) -> list[dict]:
   """Sorts students by their average grade in descending order."""
   return sorted(students_data, key=lambda x: x['average'], reverse=True)