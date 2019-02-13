import datetime
from contextlib import contextmanager


@contextmanager
def time():
    try:
        start_time = datetime.datetime.now()
        print(start_time)
        yield
    except:
        print('Ошибка')
    else:
        stop_time = datetime.datetime.now()
        print(stop_time)
        result = start_time - stop_time
        print('Время, потраченное на выполнение программы: {} секунд' .format(result.seconds))
