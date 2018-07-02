from factory.absauto import AbsAuto


class Ford(AbsAuto):
    def start(self):
        print('Ford started.')

    def stop(self):
        print('Ford stopped.')
