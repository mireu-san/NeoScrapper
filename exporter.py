import csv # a file this allows you to generate csv file based on the main.py -> from fake db (by scrapper.py)

def save_to_file(jobs):
  file = open("jobs.csv", mode="w") #mode - write
  writer = csv.writer(file)
  writer.writerow(["Title, Company, Location, Link"])
  print(jobs)
  for job in jobs:
    writer.writerow(list(job.values()))
  return