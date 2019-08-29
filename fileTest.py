import fileClassTAD as fc

day = fc.Data_day('25','2')

#criando horas para test
for id_hours in range(5,10,2):
    day.add_hours_reserved(fc.Data_hours(f'{id_hours}', None))
for id_hours in range(0,8):
    day.add_hours_reserved(fc.Data_hours(f'{id_hours}', None))

day.print_day()
day.sort_hours_reserved() #Teste de ordenação
day.print_day()

#Teste get_hours_reserved_by_id()
for h in day.get_hours_reserved_by_id('7'):
    print(h, end=' ')

print()

#Teste get_hours_reserved_by_interval()
for h in day.get_hours_reserved_by_interval('5', '7'):
    print(h, end=' ')

print()

#Teste day
print(day.name)

print("\n\n")

month = fc.Date_month('3')

month.add_day(fc.Data_day('15','2'))

print(month.get_days_by_week(3))