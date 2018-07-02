import datetime


class SimpleLogger:
    log_file = None

    @staticmethod
    def instance():
        if '_instance' not in SimpleLogger.__dict__:
            SimpleLogger._instance = SimpleLogger()
        return SimpleLogger._instance

    def open_log(self, path):
        self.log_file = open(path, 'w')

    def write_log(self, log_record):
        now = str(datetime.datetime.now())
        record = '%s: %s' % (now, log_record)
        self.log_file.writelines(record)

    def close_log(self):
        self.log_file.close()


if __name__ == '__main__':
    logger1 = SimpleLogger.instance()
    logger2 = SimpleLogger.instance()

    assert logger1 is logger2
    logger1.open_log('test.log')
    logger2.write_log('Hello World')
    logger1.close_log()
