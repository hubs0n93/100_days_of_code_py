def add(*args):
    return sum(args)


suma = add(1,1,2,2)
print(suma)


class Dupa():

    def __init__(self, **kw):
        self.equal= {"value": 5}
        self.new_equal = kw.get("value")
        self.final = 0

    def value(self):
        if self.new_equal == None:
            self.final = self.equal["value"]
        else:
            self.final = self.new_equal
        return self.final



dupa = Dupa()
print(dupa.value())
print(dupa.final)