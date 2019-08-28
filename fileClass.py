import operator


class Data_hours:
    def __init__(self, id, event):
        self.id = id
        self.event = event
    def __str__(self):
        return str(self.id)


class Data_day:
    def __init__(self, id_prin, id_sec):
        dict_days = {
            '1' : 'Domingo',
            '2' : 'Segunda',
            '3' : 'Terça',
            '4' : 'Quarta',
            '5' : 'Quinta',
            '6' : 'Sexta',
            '7' : 'Sábado'
        }
        self.id_princ = id_prin
        self.id_secund = id_sec
        self.name = dict_days[self.id_secund]
        self.hours_reserved = list()
    def add_hours_reserved(self, h):
        if (len(self.hours_reserved) <= 24):
            self.hours_reserved.append(h)
            self.sort_hours_reserved()
            return 0
        return -1

    def sort_hours_reserved(self):
        self.hours_reserved.sort(key=operator.attrgetter('id'))

    def count_hours_reserved(self):
        return len(self.hours_reserved)

    def get_hours_reserved_by_id(self, id):
        return list(filter(lambda hours: hours.id == id, self.hours_reserved))

    def get_hours_reserved_by_interval(self, start, stop):
        return list(filter(lambda hours: hours.id >= start and hours.id <= stop, self.hours_reserved))

    def print_day(self):
        for hours in self.hours_reserved:
            print(hours, end=" ")
        print()

class Date_month:
    def __init__(self, id):
        dict_month = {
            '1' : 'Jeneiro',
            '2' : 'Fevereiro',
            '3' : 'Março',
            '4' : 'Abril',
            '5' : 'Maio',
            '6' : 'Junho',
            '7' : 'Julho',
            '8' : 'Agosto',
            '9' : 'Setembro',
            '10' : 'Outubro',
            '11' : 'Novembro',
            '12' : 'Dezembro'
        }

        self.id = id
        self.nome = dict_month[id]
        self.days = list()

    def add_day(self, d):
        if len(self.days) <= self.days_limit():
            self.days.append(d)
            self.sort_days()
            return 0
        return -1

    def sort_days(self):
        self.days.sort(key=operator.attrgetter('id_princ'))

    def days_limit(self):
        if self.id in ['1', '3', '5', '7','8', '10', '12']: return 31
        elif self.id in ['4','6', '9', '11']: return 30
        else: return 28

    def get_days_by_week(self, id_semana):
        return list(filter(lambda day: day.id_princ >= id_semana*7 and day.id_princ < (id_semana+1)*7, self.days))

    def get_days_by_id(self, id):
        for day in self.days:
            if day.id_princ == id : return day
        return  -1

    def count_days(self):
        return len(self.days)

    def __str__(self):
        str_month = f"{self.nome}\n"
        list_day_reserved = [day.id_princ for day in self.days]
        cont = 0
        cont_desenho = 0
        for month in range(1, self.days_limit()+1):
            if list_day_reserved[cont] == str(month):
                str_month += f"[{month}] "
                cont+=1
            else:
                str_month += f"{month} "

            cont_desenho += 1
            if cont_desenho%7 == 0: str_month+= "\n"

        return str_month


class Agenda:
    def __init__(self):
        self.month = list()