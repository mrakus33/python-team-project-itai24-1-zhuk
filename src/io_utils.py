import os

def read_students_from_file(file_path="data/input.txt") -> list[dict]:
   """Reads student names and numeric grades from a text file."""
   students = []
   if not os.path.exists(file_path):
      print(f"Error: File {file_path} not found.")
      return students

   with open(file_path, "r", encoding="utf-8") as f:
      for line in f:
         line = line.strip()
         if not line:
            continue
         parts = line.split()
         name = parts[0]
         try:
               grades = [float(x) for x in parts[1:]]
               if not grades:
                  continue
               students.append({"name": name, "grades": grades})
         except ValueError:
               print(f"Warning: Skipping invalid data row for {name}")
               
   return students