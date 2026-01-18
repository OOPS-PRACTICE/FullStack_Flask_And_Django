class class_test:

    def instance_method(self):
        print('In the instance method')

    @classmethod
    def class_method(cls):
        print('In the class method')

    @staticmethod
    def static_method():
        print('In the static method')


cl = class_test()
cl.instance_method()

# cl.class_method()
class_test.class_method()


cl.static_method()
