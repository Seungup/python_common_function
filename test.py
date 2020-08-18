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
    # Test = [a: int=0, _b: str="0", _Test__c: bool=False]
    print(test)             # print original attr

    test.a = 99             # public  attr modification
    test._b = "1"           # protect attr modification
    test._Test__c = True    # private attr modification

    # Test = [a: int=99, _b: str="1", _Test__c: bool=True]
    print(test)             # print modified class

