import unittest
from src.analysis import calculate_average, calculate_min_max, calculate_standard_deviation

class TestAnalysisModule(unittest.TestCase):
   def test_analytics(self):
      grades = [10.0, 20.0, 30.0]
      
      self.assertEqual(calculate_average(grades), 20.0)
      self.assertEqual(calculate_min_max(grades), (10.0, 30.0))
      self.assertAlmostEqual(calculate_standard_deviation(grades), 8.1649658, places=5)

if __name__ == "__main__":
   unittest.main()