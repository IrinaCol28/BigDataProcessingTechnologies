import matplotlib
import pandas as pd
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')
# Загружаем данные из файла "Титаник.csv" в датафрейм
df = pd.read_csv("dataset/titanic.csv")

# Выводим датафрейм на экран и ознакамливаемся с его содержанием
print(df)

# Выводим первые 5 строк датафрейма
print(df.head())

# Выводим информацию о датафрейме
df.info()

# Заменяем значения в столбце "Gender" на "man" и "woman"
df['Gender'] = df['Gender'].replace({'male': 'man', 'female': 'woman'})
print(df.head(20).to_string())

# Находим максимальный возраст пассажира и выводим соответствующую строку (или строки)
max_age = df['Age'].max()
max_age_passengers = df[df['Age'] == max_age]
print("\n", max_age_passengers.to_string())

# Вычисляем среднюю стоимость билета
average_fare = df['Fare'].mean()
print(f"\nСредняя стоимость билета: {average_fare:.2f}")

# Выводим информацию о пассажирах с родственниками (SibSp или Parch больше нуля)
with_family = df[(df['SibSp'] > 0) | (df['Parch'] > 0)]
print("\n", with_family)

# Выводим всех мужчин до 50 лет и подсчитываем их количество
male_under_50 = df[(df['Gender'] == 'man') & (df['Age'] < 50)]
print(male_under_50)
print(f"Количество мужчин до 50 лет: {len(male_under_50)}")

# Сортируем датафрейм по столбцу "Pclass" в порядке возрастания
sorted_df = df.sort_values(by='Pclass')
print(sorted_df)

# С использованием функции groupby выведем информацию о количестве мужчин и женщин в каждом классе
gender_class_counts = df.groupby(['Pclass', 'Gender'])['PassengerId'].count()
print(gender_class_counts)

# Проводим анализ влияния класса пассажира на выживаемость
survival_class = df.groupby('Pclass')['Survived'].mean()
print(survival_class)

# Строим столбиковую диаграмму для наглядности
survival_class.plot(kind='bar', title='Выживаемость по классам')
plt.xlabel('Класс')
plt.ylabel('Процент выживших')
plt.show()
