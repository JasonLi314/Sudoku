class C:
    def __init__(self, x):
        self.x = x

    def __eq__(self, other):
        print("equals operator")
        return self.x == other.x

c1 = C(10)
c2 = [C(11)] * 10
c2[9] = C(10)
print(c1 in c2)