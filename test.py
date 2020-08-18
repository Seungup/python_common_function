import common_functions as cf


class Test:
    """
    Test Class
    """

    def __init__(self):
        self.a: int = 0
        self._b: str = "0"
        self.__c: bool = False

    def __str__(self):
        return cf.__class_attr_to_str__(self)


if __name__ == '__main__':
    test = Test()
    print(test)             # print original attr
    test.a = 99             # public  attr modification
    test._b = "1"           # protect attr modification
    test._Test__c = True    # private attr modification
    print(test)             # print modified class
