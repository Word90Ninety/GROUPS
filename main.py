print(__name__)

from group import Group
from cayley_tabler import cayley_tabler, xor
from permutator import permuter, even_permuter, permutation_composer
from group_composer import direct_group_product

topic = "perms"

if __name__ == "__main__":
  if topic == "cayley":
    table = cayley_tabler(Group([1, 2], xor), True, True)
    for row in table:
      print(row)
  elif topic == "product":
    direct_group_product(1, 1)
  elif topic == "perms":
    perms = cayley_tabler(Group(permuter(4), permutation_composer), True, True)
    for line in perms:
        print(line)
  elif topic == "eperms":
    evens = cayley_tabler(Group(even_permuter(4), permutation_composer), True, True)
    for line in evens:
        print(line)
    