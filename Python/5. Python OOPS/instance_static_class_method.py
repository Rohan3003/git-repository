class MyClass:
    def method(self):
        return 'instance method called', self

    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'

if __name__ == '__main__':
    # creating an instance of class
    # obj = MyClass()

    # calling instances 
    # print(obj.method())
    # print(obj.classmethod())
    # print(obj.staticmethod())

    # calling methods without creating an intance directly through the class
    print(MyClass.classmethod())
    print(MyClass.staticmethod())
    print(MyClass.method())