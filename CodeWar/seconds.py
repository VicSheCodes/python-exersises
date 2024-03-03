from datetime import datetime


def make_readable(seconds = 359999, TIME_FORMAT= '%H:%M:%S'):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    second = seconds % 60
    print(f'{hours:02d}:{minutes:02d}:{second:02d}')
    pass

if __name__ == '__main__':
    make_readable()