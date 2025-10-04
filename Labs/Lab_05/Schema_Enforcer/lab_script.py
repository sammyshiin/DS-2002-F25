#!/usr/bin/env python3

import csv
import json
import pandas as pd

#Task 1: Create the Tabular CSV Data (Requires Cleaning)
raw_csv_filename = "raw_survey_data.csv"

csv_headers = ["student_id", "major", "GPA", "is_cs_major", "credits_taken"]

raw_data = [
    [100, "Philosophy", 3, "No", "13.0"],            
    [101, "Computer Science", 3.8, "Yes", "14"],      
    [102, "Religious Studies", 2, "No", "15"],      
    [103, "Data Science", 3.6, "No", "16"],          
    [104, "English", 4, "No", "18"]
]
with open(raw_csv_filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(csv_headers)
    writer.writerows(raw_data)
print(f"Created {raw_csv_filename}")

#Task 2: Create the Hierarchical JSON Data (Requires Normalization)
raw_json_filename = "raw_course_catalog.json"
courses = [
  {
    "course_id": "DS2002",
    "section": "001",
    "title": "Data Science Systems",
    "level": 200,
    "instructors": [
      {"name": "Austin Rivera", "role": "Primary"}, 
      {"name": "Heywood Williams-Tracy", "role": "TA"} 
    ]
  },
  {
    "course_id": "SDE3140",
    "section": "001",
    "title": "Software Development Essentials",
    "level": 300,
    "instructors": [
        {"name": "Rich Nguyen", "role": "Primary"}
    ]
  },
  {
    "course_id": "PHIL1410",
    "section": "001",
    "title": "Forms of Reasoning",
    "level": 100,
    "instructors": [
        {"name": "Trey Boone", "role": "Primary"}
    ]
  }
]

with open(raw_json_filename, "w") as f:
    json.dump(courses, f, indent=2)
print(f"Created {raw_json_filename}")

#Task 3: Clean and Validate the CSV Data
clean_csv_filename = "clean_survey_data.csv"
df = pd.read_csv(raw_csv_filename)

df["is_cs_major"] = df["is_cs_major"].replace({"Yes": True, "No": False})
df = df.astype({"GPA": "float64", "credits_taken": "float64"})
df.to_csv(clean_csv_filename, index=False)
print(f"Cleaned and saved {clean_csv_filename}")

#Task 4: Normalize the JSON Data
clean_json_csv_filename = "clean_course_catalog.csv"
with open(raw_json_filename, "r") as f:
    data = json.load(f)
df_courses = pd.json_normalize(
    data,
    record_path=["instructors"],
    meta=["course_id", "title", "level"]
)
df_courses.to_csv(clean_json_csv_filename, index=False)
print(f"Normalized and saved {clean_json_csv_filename}")
