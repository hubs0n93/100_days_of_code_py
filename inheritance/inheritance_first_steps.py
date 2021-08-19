class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breath(self):
        print('inhale exhale')


class Fish(Animal):
    def __init__(self):
        super().__init__()


    def breath(self):
        super().breath()
        print('doing this underwater')

    def swim(self):
        print('swimming')


    def new_num_of_eyes(self):
        print(self.num_eyes + 1)

nemo = Animal()
print(nemo.num_eyes)
nemo.breath()
print("\n\n*****Inheritance, creating the new Class Fish\n")

new_nemo = Fish()
print(new_nemo.num_eyes)
new_nemo.breath()
new_nemo.swim()
new_nemo.new_num_of_eyes()


