list1 = [("Jon",15), ("Ned",45), ("Arya",9), ("Catelyn",44), ("Bran",10)]

for a, b in list1:
  if b > 18:
    print(a)
#New example

books = ["ULYSSES","ANIMAL FARM","BRAVE NEW WORLD","ENDER'S GAME"]
book_dict = {}

for i in books:
  key = i
  value1 = len(i)
  value2 = len(set(i))
  value3 = (value1+value2)/2
  book_dict[i] = value1,value2,value3

print(book_dict)