class Device:
    def __init__(self,name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name}, {self.connected_by}"
    
    def disconnected(self):
        self.connected = False
        print("Disconnected")

class Printer(Device):
    def __init__(self, name, connected_by, capacity):
        super().__init__(name, connected_by)
        self.capacity = capacity

    def __str__(self):
        return f"{super().__str__()} ({self.capacity})" 

    def print(self, pages):
        if not self.connected:
            print('your printer is not connected')   
            return
        print('printer is connected') 


printer = Printer("Printer","USB", 50)   
printer.print(20)

# # print(printer)

# printer.disconnected()

# # print(printer)
# printer.print(20)


class A:
    def show(self):
        print("A")
        super().show()

class B:
    def show(self):
        print("B")
        super().show()

class C(A, B):
    def show(self):
        print("C")
        super().show()

class Base:
    def show(self):
        print("Base")

class D(C, Base):
    pass

D().show()

# Method Resolution Order (MRO) 

# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         print("B")

# class C(A):
#     def show(self):
#         print("C")

# class D(B, C):
#     pass

# D().show()

# print(D.__mro__)


class A:
    def show(self):
        print('A')

class B:
    def show(self):
        print('B')

class C(A,B):
    def show(self):
        super().show()


c = C()
c.show()
print(C.__mro__)
