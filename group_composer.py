
from group import Group
from cayley_tabler import cayley_tabler

print("ding")


def direct_group_product(group1, group2):
  cartesianProduct = []
  for first in group1.set:
      for second in group2.set:
          pair = [first, second]
          cartesianProduct.append(pair)

  def compositeOperation(pair1, pair2):
      return([group1.op(pair1[0], pair2[0]), group2.op(pair1[1], pair2[1])])

  directProduct = Group(cartesianProduct, compositeOperation)
  return(directProduct)

def xor(first, second):
  if first == second:
      return(1)
  else:
      return(2)
  
def tri_rotate(first, second):
  return((first+second)%3+1)










if __name__ == "__mai__":
  z2 = Group([1, 2], xor)

  unexplored = direct_group_product(direct_group_product(z2, z2), z2)
  exploration = cayley_tabler(unexplored, True)
  for line in exploration:
      print(line)
elif __name__ == "__group_composer__":
  z3 = Group([1, 2, 3], tri_rotate)
  triple = cayley_tabler(z3)
  for row in triple:
      print(row)
      
  z3xz3 = direct_group_product(z3, z3)
  cross_tri = cayley_tabler(z3xz3, True)
  for row in cross_tri:
      print(row)
















  
