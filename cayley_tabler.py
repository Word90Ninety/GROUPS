print(__name__)

from group import Group

def cayley_tabler(group, simplify=False, trim=False):
  rows = []

  blank = ""
  length = len(str(group.set[0]))
  if length == 1:
    blank = 0
  elif type(group.set[0]) != str:
    for i in range(length - 2):
      blank = blank + "0"
  else:
    for i in range(length):
      blank = blank + "0"
  
  if trim == False:
    row = [blank]
    for element in group.set:
      row.append(element)
    rows.append(row)
  
  for another in group.set:
    if trim == False:
      row = [another]
    else:
      row = []
    for yetAnother in group.set:
      row.append(group.op(another, yetAnother))
    rows.append(row)

  if simplify == True:
    simpleTable = []
    for row in rows:
        simpleRow = []
        for element in row:
            if element == blank:
                simpleElement = 0
            else:
                for i in range(len(group.set)):
                  if str(element) == str(group.set[i]):
                    simpleElement = int(i + 1)
            simpleRow.append(simpleElement)
        simpleTable.append(simpleRow)
    return(simpleTable)
  else:
    return(rows)


#print a row that's just X and then the elements
#print rows


def xor(first, second):
  if first == second:
    return (1)
  else:
    return (2)
"""
if __name__ == "cayley_tabler":
  print("ding")
  table = cayley_tabler(Group([1, 2], xor), True)
  for row in table:
    print(row)
"""