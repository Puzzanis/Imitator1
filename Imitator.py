import uuid


def analog():
    inc = 2
    ana1 = ''
    for i in range(inc):
        uid = str(uuid.uuid4()).upper()
        ana = """Пересчет: TScaler @ {{{0}}}
                \t\tвход: TIJoint | Double; 4000;;
                \t\tминимум входа: TMJoint | Double; 0;;
                \t\tмаксимум входа: TMJoint | Double;100;;
                \t\tминимум выхода: TMJoint | Double;0;;
                \t\tмаксимум выхода: TMJoint | Double;100;;
                \t\tусекатьзначение: TIJoint | Boolean;0;;
                \t\tвыход: TQJoint | Double; 4000;;
                \t\tзначение достоверно: TQJoint | Boolean;0;;
                \t\tниже минимума(обрыв): TQJoint | Boolean;0;;
                \t\tвыше макимума(КЗ): TQJoint | Boolean;1;;
                \t\tвыход за ранги пересчета: TQJoint | Boolean; 1;;
                \t\tпределы: TJntGroup
                    \t\t уставка максимально аварийная: TMJoint | Double; 95;;
                    \t\t уставка максимально предельная: TMJoint | Double; 90;;
                    \t\t уставка минимально предельная: TMJoint | Double; 10;;
                    \t\t уставка минимальноаварийная: TMJoint | Double; 5;;
                    \t\t максимально аварийное значение: TQJoint | Boolean; 1;;
                    \t\t максимально предельное значение: TQJoint | Boolean; 1;;
                    \t\t нормальное значение: TQJoint | Boolean; 0;;
                    \t\t минимально предельное значение: TQJoint | Boolean; 0;;
                    \t\t минимально аварийное значение: TQJoint | Boolean; 0;;
                \t\tend
            \t\tend\n\t\t\t\t\t""".format(uid)
        ana1 += ana
    return str(ana1)


def encoder():
    return ''


def decoder():
    return ''


def imitator():
    uid = str(uuid.uuid4()).upper()
    tcp = """Imitator 1.1
            Модель: TGroup
                ModBus TCP Client: TModBusTCPClient @{{{0}}}
                    параметры
                        записывать протокол обмена в файл | ;;
                        отображаемых записей в протоколе обмена | 50;50;[0..1000]
                        формат отображения времени | h:mm:ss;h:mm:ss;h:mm:ss, d.mm.yy h:mm:ss, h:mm:ss.zzz
                        порт | 502;502;[1..65535]
                        сервер | 192.0.0.1;127.0.0.1;
                        количество ожидаемых байт в кадре | 512;512;[1..512]
                        начальный адрес в сегментах | 1;1;0, 1
                        таймаут ответа (мс) | 500;500;[1..60000]
                        период поллинга (мс) | 5;5;[0..60000]
                        всегда использовать множественную запись | да;да;да, нет
                        максимальное количество слов данных в запросе | 125;125;[1..125]
                        подключаться как Concept | нет;нет;да, нет
                        блокировать ячейки при записи | нет;нет;да, нет
                        количество одновременных транзакций | 4;4;1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
                    end
                    станции
                    end
                end
                Преобразователи: TGroup
                    Шифраторы: TGroup
                    {1}
                    end
                    Дешифраторы: TGroup
                    {2}
                    end
                end
                Аналоги: TGroup
                    {3}
                end
                Агрегаты: TGroup
                    {4}
                end
                Задвижки: TGroup
                    {5}
                end
                Вспомсистемы: TGroup
                    {6}
                end
             end
            Параметры выполнения
                Длительность цикла (мс) | 200;200;
                Точность вычислений | 8;8;2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
            end
        end""".format(uid, None, None, analog(), None, None, None)
    return tcp
