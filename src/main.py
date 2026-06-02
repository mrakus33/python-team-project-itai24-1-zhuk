import os
from io_utils import read_students_from_file
from analysis import calculate_average, calculate_min_max, calculate_standard_deviation, sort_students

def main():
   print("Team Data Analyzer Program ")
   raw_data = read_students_from_file()
   
   if not raw_data:
      print("No student data to process. Exiting.")
      return
      
   processed_students = []
   for student in raw_data:
      grades = student["grades"]
      avg = calculate_average(grades)
      minimum, maximum = calculate_min_max(grades)
      std_dev = calculate_standard_deviation(grades)
      
      processed_students.append({
         "name": student["name"],
         "average": avg,
         "min": minimum,
         "max": maximum,
         "std_dev": std_dev
      })
      
   sorted_result = sort_students(processed_students)
   divider = "=" * 50 + "\n"
   header = f"{'Name':<10} | {'Average':<8} | {'Min':<5} | {'Max':<5} | {'Std Dev':<8}\n"
   output_content = divider + header + divider
   for student in sorted_result:
      output_content += f"{student['name']:<10} | {student['average']:<8.2f} | {student['min']:<5.1f} | {student['max']:<5.1f} | {student['std_dev']:<8.2f}\n"
   output_content += divider
   print(output_content)
   os.makedirs("data", exist_ok=True)
   with open("data/output.txt", "w", encoding="utf-8") as f:
      f.write(output_content)
   print("Results successfully saved to data/output.txt")

if __name__ == "__main__":
   main()