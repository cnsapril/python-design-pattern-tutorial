import datetime

from singleton.metaclass.singleton_meta import Singleton


class Logger(metaclass=Singleton):
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
    logger = Logger('test.log')
    logger1 = Logger('test1.log')
    logger.write_log('Hello hello hey')
    logger1.write_log('Pick me pick me up')
    logger.close_log()
