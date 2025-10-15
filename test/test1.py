class A:
    _field: int
    
    def run(self) -> None:
        self._field = 5
        print(self._field)

class B:
    _field: int
    
    def __init__(self, value: int) -> None:
        self._field = value
    
    def run(self) -> None:
        self._field = 10
        print(self._field)

def main() -> None:
    a = A()
    a.run()
    
    b = B(3)
    b.run()
    print(b._field)
    print(a._field)

if __name__ == '__main__':
    main()
