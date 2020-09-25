print(__name__)

from group import Group
from cayley_tabler import cayley_tabler, xor
from permutator import even_permuter, permutation_composer

topic = "cayley"

if __name__ == "__main__":
  if topic == "cayley":
    table = cayley_tabler(Group([1, 2], xor), True, False)
    for row in table:
      print(row)
  elif topic == "perms":
    evens = cayley_tabler(Group(even_permuter(4), permutation_composer))
    for line in evens:
        print(line)