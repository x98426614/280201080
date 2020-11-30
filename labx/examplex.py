file_path = "members.txt"
file = open(file_path)
each_line = file.readline()
dictionary = {}
counter = True
while counter:
  name = each_line.split(": ")[0]
  email = each_line.split(": ")[1]
  a = name
  b = email
  c = {a,b}
  dictionary.update(c)
  if each_line == "\n":
    counter = False


























#Purpose of this file and folder is to test bottom line codes.