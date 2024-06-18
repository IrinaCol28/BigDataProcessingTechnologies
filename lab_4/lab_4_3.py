import matplotlib
import matplotlib.pyplot as plt
from numpy import *

matplotlib.use('TkAgg')

# Объёмы продаж предпирятий
mes = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь']
y_first_company = random.uniform(10, 55, size=6)
y_second_company = random.uniform(10, 55, size=6)

# Размеры рисунка и отступы подграфиков
fig, axs = plt.subplots(2, 2, figsize=(10, 11))
plt.subplots_adjust(wspace=0.4, hspace=0.4)

# Первый подграфик в виде линий
axs[0, 0].plot(mes, y_first_company, '--.r', label='Предприятие 1')
axs[0, 0].plot(mes, y_second_company, '--.b', label='Предприятие 2')
axs[0, 0].legend()
axs[0, 0].set_xlabel('Месяцы')
axs[0, 0].set_ylabel('Объемы продаж, тыс. шт.')
axs[0, 0].set_title('Объемы продаж предприятий \n(графики в виде линий)', fontsize='14', color='black')
axs[0, 0].grid()

# Второй подграфик в виде столбцов
x = arange(1, len(mes) + 1)
width = 0.3
axs[0, 1].bar(x, y_first_company, width=width, label='Предприятие 1')
axs[0, 1].bar(x + width, y_second_company, width=width, label='Предприятие 2')
axs[0, 1].set_xticks(x + width / 2, mes)
axs[0, 1].legend()
axs[0, 1].set_xlabel('Месяцы')
axs[0, 1].set_ylabel('Объемы продаж, тыс. шт.')
axs[0, 1].set_title('Объемы продаж предприятий \n(графики в виде столбцов)', fontsize='14', color='black')
axs[0, 1].grid()

# Третий подграфик в виде круговой диаграммы
axs[1, 0].pie(y_first_company, labels=mes, autopct='%1.2f%%', counterclock=False)
axs[1, 0].set_title('Объемы продаж 1-го предприятия', fontsize='14', color='black')

# Четвёртый подграфик в виде круговой диаграммы
axs[1, 1].pie(y_second_company, labels=mes, autopct='%1.2f%%', counterclock=False)
axs[1, 1].set_title('Объемы продаж 2-го предприятия', fontsize='14', color='black')

# Отображение рисунков с графиками
plt.show()
