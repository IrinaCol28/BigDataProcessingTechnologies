import pandas as pd
# pip install openpyxl

# Загрузка данных из csv-файла
df = pd.read_csv("dataset/raw.githubusercontent.com_dm-fedorov_pandas_basic_master_data_new_year_film.csv")

# Вывод содержимого файла
print(df.to_string())

# Вывод 5-ти первых строк
print("\n", df.head(5).to_string(), "\n")

# Вывод информации о датафрейме
df.info()

# Вывод кол-ва строк и столбцов
print("\nКол-во строк: ", df.shape[0])
print("Кол-во столбцов: ", df.shape[1])

# Вывод названия столбцов
print("\nНазвания столбцов: ", df.columns)

# Вывод индексов строк
print("\nИндексы строк: ", df.index)

# Вывод датафрейма в виде массива
print("\n", df.to_numpy())

# Вывод типа данных для каждого столбца
print("\n", df.dtypes)

# Вывод массива уникальных значений в столбце country
print("\nМассива уникальных значений в столбце country:", df['country'].unique())

# Вывод кол-ва уникальных значений в каждом столбце
print("\n", df.nunique())

# Вывод кол-ва пропущенных значений в каждом столбце
print("\n", df.isnull().sum())

# Удаление строк с пропущенными значениями
df = df.dropna()
print("\n", df)

# Удаление дубликатов строк
if df.duplicated().sum() > 0:
    print("\nЕсть дубликаты строк")
    df = df.drop_duplicates()
else:
    print("\nНет дубликатов строк")
print(df)

# Переименование столбцов name и country
df.rename(columns={'name': 'название', 'country': 'страна'}, inplace=True)
print("\n", df)

# Удаление последнего столбца и вставка в начало
last_column = df.iloc[:, -1]
df = df.iloc[:, :-1]
df.insert(0, last_column.name, last_column)
print("\n", df)

# Удаление 20-ти последних строк
df = df.drop(df.index[-20:])
print("\n", df)

# Формирование нового датафрема и вывод его в Excel
df2 = df.iloc[:10, :3]
df2.to_excel("df2.xlsx", index=False)


