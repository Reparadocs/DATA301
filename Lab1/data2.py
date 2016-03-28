import csv

class Name:
  def __init__(self, name, year, gender, count):
    self.name = name
    self.year = int(year)
    self.count = int(count)
    self.gender = gender

def ending_is_vowel(name):
  last_char = name[-1:]
  if last_char == 'a' or last_char == 'e' or last_char == 'i' or last_char == 'o' or last_char == 'u':
    return True
  return False

names = []
result_dict = {}
total_dict = {}
with open('names2014.csv', 'rb') as csvfile:
  namesreader = csv.reader(csvfile, delimiter=',')
  for name in namesreader:
    if name[0] == 'Id':
      continue
    obj = Name(name[1], name[2], name[3], name[4])
    names.append(obj)

result_dict['M'] = 0
result_dict['F'] = 0
total_dict['M'] = 0
total_dict['F'] = 0

for name in names:
  if ending_is_vowel(name.name):
    result_dict[name.gender] += name.count
  total_dict[name.gender] += name.count

print result_dict
print total_dict
