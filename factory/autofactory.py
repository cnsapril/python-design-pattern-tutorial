from inspect import getmembers, isclass, isabstract
import factory
from factory.absauto import AbsAuto


class AutoFactory:
    # key -> value pair. Key is the automobile's name (string) and value is a reference to the subclass
    autos = {}

    def __init__(self):
        self._load_autos()

    def _load_autos(self):
        classes = getmembers(factory, lambda c: isclass(c) and not isabstract(c))

        for name, _type in classes:
            if isclass(_type) and issubclass(_type, AbsAuto):
                self.autos[name] = _type

    def create_instance(self, auto_name):
        if auto_name in self.autos:
            return self.autos[auto_name]()
        else:
            raise TypeError('Invalid class name {}'.format(auto_name))


if __name__ == '__main__':
    factory = AutoFactory()

    cars = ['Toyota', 'Ford']
    for car_name in cars:
        car = factory.create_instance(car_name)
        car.start()
        car.stop()
