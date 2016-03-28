import csv

class Name:
  def __init__(self, name, year, gender, count):
    self.name = name
    self.year = int(year)
    self.count = int(count)
    self.gender = gender

class NameResult:
  def __init__(self, count, gender):
    if gender == 'M':
      self.male = count
    else:
      self.female = count
    self.total = 0
    self.percentage_male = 0
    self.percentage_female = 0

  def complete(self, count, gender):
    if gender == 'M':
      self.male = count
    else:
      self.female = count
    self.calculateTotal()

  def calculateTotal(self):
    self.total = self.male + self.female
    self.percentage_male = float(self.male) / float(self.total)
    self.percentage_female = float(self.female) / float(self.total)

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
  if name.name in result_dict:
    result_dict[name.name].complete(name.count, name.gender)
  else:
    result_dict[name.name] = NameResult(name.count, name.gender)

with open('result4.csv', 'w') as writecsv:
  csvwriter = csv.writer(writecsv, delimiter=',')
  csvwriter.writerow(['Name', 'Percent Male', 'Percent Female'])
  for key in result_dict:
    csvwriter.writerow([key, result_dict[key].percentage_male, result_dict[key].percentage_female])

