import re
from functools import reduce
from operator import mul

print(sum(list(map(lambda s: reduce(mul, list(map(int, (re.findall("[0-9]+", s))))), [op for op in re.findall("mul\([0-9]+,[0-9]+\)", ''.join(re.split("don't\(\)(.|\n)*?do\(\)" ,open("input.txt", "r").read())))]))))