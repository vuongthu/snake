class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish(Animal):
    def __init__(self):
        # Anything created in this Fish class will inherit all the attributes and methods created in Animal class
        super().__init__()

    # What if we wanted to define the breathe function a little more? Same functionality as the super class, but more
    def breathe(self):
        super().breathe()  # We call super and the method, and extend the functionality below
        print("Doing this underwater.")

    def swim(self):
        print("Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()
# print(nemo.num_eyes)
