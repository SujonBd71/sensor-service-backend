
def event(y):
    if y == 20:
        yield y*y

d1 = event(21)
print(next(d1))
d2 = event(20)
print(d2)


