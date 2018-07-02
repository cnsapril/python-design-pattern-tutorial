from factory.absauto import AbsAuto


class Toyota(AbsAuto):
    def start(self):
        print('Toyota started.')

    def stop(self):
        print('Toyota stopped.')
