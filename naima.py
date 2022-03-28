class One:
    def __init__(self, a):
        self.a = a

    def __add__(self, object2):
        return self.a + object2.a


class Two:
    def __init__(self, a):
        self.a = a

    def __add__(self, object2):
        return self.a + object2.a


a_instance = One(10)
b_instance = Two(20)
print(a_instance + b_instance)
