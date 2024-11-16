import math
import adj
i = 325489
s = (math.ceil(math.sqrt(i)))
if s%2 == 0:
    s += 1
d = (s**2)-i
d1 = s-d
m = math.ceil(s/2)
print(m-d1+m-1)


#oeis a141481 = 330785

