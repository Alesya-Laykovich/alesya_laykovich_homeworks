"""6. Написать функцию и сделать так, чтобы число секунд отображалось в виде:
дни:часы:минуты:секунды."""
import time


def time_function(new_time):
    time_format = time.strftime('%H:%M:%S', time.gmtime(time_in_sec))
    return time_format


time_in_sec = int(input('Введите количество секунд: '))
print(f'Время: {time_function(time_in_sec)}')
