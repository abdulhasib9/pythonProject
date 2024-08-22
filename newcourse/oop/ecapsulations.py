class Test:
    def __init__(self,name) -> None:
        self.__name = name
        
    def __str__(self) -> str:
        return f"{self._name}"
    def set_name(self,value):
        self.name = value
    def get_name(self):
        return self.name
    
    name =property(get_name,set_name)
jhon = Test('Jhon')

jhon.set_name('test')
jhon.get_name()
