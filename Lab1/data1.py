import csv

class Name:
  def __init__(self, name, year, gender, count):
    self.name = name
    self.year = int(year)
    self.count = int(count)
    self.gender = gender

names_dict = {}
result_dict = {}
with open('names1000.csv', 'rb') as csvfile:
  namesreader = csv.reader(csvfile, delimiter=',')
  for name in namesreader:
    if name[0] == 'Id':
      continue
    obj = Name(name[1], name[2], name[3], name[4])
    if obj.year in names_dict:
      names_dict[obj.year].append(obj)
    else:
      names_dict[obj.year] = [obj,]

for year in names_dict:
  tot_length = 0
  num_names = 0
  for name in names_dict[year]:
    tot_length += name.count * len(name.name)
    num_names += name.count
  result_dict[year] = float(tot_length) / float(num_names)

with open('result1.csv', 'w') as writecsv:
  csvwriter = csv.writer(writecsv, delimiter=',')
  csvwriter.writerow(['Year', 'Avg Length'])
  for key in result_dict:
    csvwriter.writerow([key, result_dict[key]])




