import csv

def save_to_file(one_company):
  name = one_company['name']
  jobs_list = one_company['jobs']
  file = open(f"{name}.csv", mode="w", encoding="utf-8")
  writer = csv.writer(file)
  writer.writerow(["place", "title", "time", "pay", "date"])
  for job in jobs_list:
    writer.writerow(job) 
  # return 