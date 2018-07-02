import datetime

from singleton.baseclass.singleton_base import Singleton


class Logger(Singleton):
    log_file = None

    def __init__(self, path):
        if self.log_file is None:
            self.log_file = open(path, 'w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s: %s\n' % (now, log_record)
        self.log_file.write(record)

    def close_log(self):
        self.log_file.close()
        self.log_file = None


if __name__ == '__main__':
    logger1 = Logger('test.log')
    logger2 = Logger('test1.log')

    assert logger1 is logger2
