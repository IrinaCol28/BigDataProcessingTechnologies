from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# Созданние сессии
spark = SparkSession.builder.master("local[*]").appName("SparkExamples").getOrCreate()

# Чтение данных
csv_file = 'data/stocks_price_final.csv'
df = spark.read.csv(csv_file, header=True)

# Вывод схемы
df.printSchema()

# Изменение типов данных
df = df.withColumn("_c0", df._c0.cast("Integer"))
df = df.withColumn("date", df.date.cast("Date"))
df = df.withColumn("open", df.open.cast("Double"))
df.printSchema()

# Определение новой схемы через StructType
data_schema = [StructField("_c0", IntegerType(), True),
               StructField("symbol", StringType(), True),
               StructField("date", DateType(), True),
               StructField("open", DoubleType(), True),
               StructField("high", DoubleType(), True),
               StructField("low", DoubleType(), True),
               StructField("close", DoubleType(), True),
               StructField("volume", IntegerType(), True),
               StructField("adjusted", DoubleType(), True),
               StructField("market.cap", StringType(), True),
               StructField("sector", StringType(), True),
               StructField("industry", StringType(), True),
               StructField("exchange", StringType(), True), ]

final_struc = StructType(fields=data_schema)
df2 = spark.read.csv(csv_file, header=True, schema=final_struc)
df2.printSchema()

# dtypes
print(df2.dtypes)

# head
print(df2.head(3))

# show
df2.show(3)

# first
print(df2.first())

# take
print(df2.take(3))

# take
df2.describe('_c0').show()

# columns
print(df2.columns)

# count
print(df2.count())

# distinct
print(df2.distinct().count())

# limit
df3 = df2.limit(8)
df3.show()
print(df3.count())

# Добавление столбца
df2.withColumn('Разность', df3.high - df2.low).show(5, truncate=8)

# Сортировка
df2.orderBy(desc('_c0')).show(5, truncate=9)

# Выбор одного столбца
df2.select('sector').show(5)

# Выбор нескольких столбцов
df2.select(['open', 'close', 'adjusted']).show(5)

# Фильтр
df2.filter((df2.date >= '2020-01-01') & (df2.date <= '2020-01-31')).show(5)
df2.filter(df2.adjusted.between(100.0, 500.0)).show(5)

# when
df2.select('open', 'close', 'adjusted', when(df2.adjusted <= 55.0, 'Цена низкая').otherwise('Цена высокая')
           .alias('Анализ цены')).show(5)
df2.select('open', 'close', 'adjusted', when(df2.adjusted <= 55.0, 'Цена низкая').alias('Анализ цены')).show(5)
df2.select('open', 'close', 'adjusted',
           when(df2.adjusted <= 55.0, 'Цена низкая').when(df2.adjusted.between(55, 60), 'Цена средняя').when(
               df2.adjusted > 60, 'Цена высокая').alias('Анализ цены')).show(5)

# like
df2.select('sector', df2.sector.rlike('^[B,C]').alias('Колонка sector начинается с B или C')).distinct().show()

# groupby
df2.select(['industry', 'open', 'close', 'adjusted']).groupby('industry').mean().show()

# agg
df2.filter((df2.date >= '2020-01-01') & (df2.date <= '2020-01-31')).groupby('sector') \
    .agg(
    min('date').alias('С'),
    max('date').alias('По'),

    min("open").alias('Open min'),
    max("open").alias('Open max'),
    avg("open").alias('Open среднее'),

    min("close").alias('Close min'),
    max("close").alias('Close max'),
    avg("close").alias('Close среднее'),
).show()

# Collect
df3.select('open', 'close', 'volume').show()
print(df3.select('open', 'close', 'volume').collect())
print(df3.select('open', 'close', 'volume').collect()[0])
print(df3.select('open', 'close', 'volume').collect()[0][0])
df2.select(sum('low').alias('Сумма')).show()
print(df2.select(sum('low').alias('Сумма')).collect())
print(df2.select(sum('low').alias('Сумма')).collect()[0][0])

# join
df4 = df3.select('_c0', 'open', 'close')
df5 = df3.select('_c0', 'sector')
df4.join(df5, '_c0').show()

df6 = df4.withColumnRenamed('_c0', 'Номер')
df6.join(df5, df6.Номер == df4._c0).show()

# toPandas
print(df3.toPandas().head(5))

# Визуализация
df3.toPandas().plot(title='График изменения цены', x='date', y=['open', 'close'], figsize=(8, 4))
df3.toPandas().plot(title='График изменения цены', x='date', y=['open', 'close'], kind='bar', figsize=(8, 4))
plt.show()

# Запись в файл

df2.write.csv('dataset.csv')

df2.select(['date', 'open', 'close', 'adjusted']).write.save('dataset2.csv', format='csv')
