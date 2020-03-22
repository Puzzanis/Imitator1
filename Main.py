import timeit
import time
import pandas as pd
import Imitator


def read_Excel(file, sheets):
    df = pd.read_excel(file, sheets)
    return df


def func(name, sheet):
    a = Imitator.imitator()
    lis_t = []
    df_list = read_Excel(name, sheet)
    with open('Imitator.imod', 'w', encoding='cp1251') as out:
        csv_out = out.write(a)
    return df


def main(name):
    start_time = timeit.default_timer()
    sheet_name = ['Таблица сигналов', 'Аналоговые сигналы', 'Сост. МПНА', 'Сост. задвижек', 'Сост. вспомсистем']
    func(name,  sheet_name)
    stop_time = timeit.default_timer()
    print(stop_time - start_time)


if __name__ == '__main__':
    from tkinter import *
    from tkinter import filedialog as fd


    def open_file():
        # Tk().withdraw()
        # file_name = fd.askopenfilename()
        file_name = 'Переменные_Горький ПНС_ЧРП_19 -NEW.xls'
        return file_name

    main(open_file())
