import csv

class Name:
  def __init__(self, name, year, gender, count):
    self.name = name
    self.year = int(year)
    self.count = int(count)
    self.gender = gender


names = []
result_dict = {}
with open('names2014.csv', 'rb') as csvfile:
  namesreader = csv.reader(csvfile, delimiter=',')
  for name in namesreader:
    if name[0] == 'Id':
      continue
    obj = Name(name[1], name[2], name[3], name[4])
    names.append(obj)

for name in names:
  for i in xrange(len(name.name)):
    if name.name[i].upper() in result_dict:
      result_dict[name.name[i].upper()] += name.count
    else:
      result_dict[name.name[i].upper()] = name.count

with open('result3.csv', 'w') as writecsv:
  csvwriter = csv.writer(writecsv, delimiter=',')
  for key in result_dict:
    csvwriter.writerow([key, result_dict[key]])


