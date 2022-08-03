class Car():
    manufactory = None  # 類屬性
    
    def __init__(self, manufactory):
        self.manufactory = manufactory  # 實體屬性
    
    def func1(self):  # 實體方法
        """ 這邊的 self 指向實例化後的物件自己 """
        print("Instance Method")
        print(self.manufactory)
    
    @classmethod
    def func2(cls):  # 類方法
        """ 這邊的 cls 指向物件本身 """
        print("Class Method")
        print(cls.manufactory)
    
    @staticmethod
    def func3():  # 靜態方法
        print("Static Method")


class SUV(Car):  # 繼承
    _car_type = "SUV"  # 封裝
    
    def __init__(self, manufactory):
        super().__init__(manufactory)  # 實體屬性
    
    @classmethod
    def get_car_type(cls):
        print(cls.car_type)
    
    def func1(self, value):  # 複寫
        print(value)
    
    @staticmethod
    def func4(val1, val2=None, val3=None):  # 多載
        print(val1, val2, val3)


if __name__ == "__main__":
    bmw = SUV("BMW")
    bmw.get_car_type()
    bmw.func1("test")
    bmw.func4(123)
    bmw.func4(123, 456)
    bmw.func4(123, 456, 789)