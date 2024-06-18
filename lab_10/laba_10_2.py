from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use('TkAgg')

# Созданние сессии
spark = SparkSession.builder.master("local[*]").appName("SparkExamples").getOrCreate()

# Чтение данных
csv_taxi_zone = 'data/taxi_zone_lookup.csv'
csv_yellow_tripdata = 'data/yellow_tripdata_2020-06.csv'
df_trip = spark.read.csv(csv_yellow_tripdata, header=True)
df_zone = spark.read.csv(csv_taxi_zone, header=True)

# Кол-во строк
print('Кол-во строк в yellow_tripdata: ', df_trip.count())
print('Кол-во строк в taxi_zone_lookup: ', df_zone.count())

# Первые 10 строк
print('Первые 10 строк yellow_tripdata')
df_trip.show(10)
print('Первые 10 строк taxi_zone_lookup')
df_zone.show(10)

# Схемы датасетов
print('Схема yellow_tripdata')
df_trip.printSchema()
print('Схема taxi_zone_lookup')
df_zone.printSchema()

# Изменение типов данных
df_trip = df_trip.withColumn("VendorID", df_trip.VendorID.cast("Integer"))
df_trip = df_trip.withColumn("tpep_pickup_datetime", df_trip.tpep_pickup_datetime.cast("Timestamp"))
df_trip = df_trip.withColumn("tpep_dropoff_datetime", df_trip.tpep_dropoff_datetime.cast("Timestamp"))
df_trip = df_trip.withColumn("passenger_count", df_trip.passenger_count.cast("Integer"))
df_trip = df_trip.withColumn("trip_distance", df_trip.trip_distance.cast("Double"))
df_trip = df_trip.withColumn("RatecodeID", df_trip.RatecodeID.cast("Integer"))
df_trip = df_trip.withColumn("store_and_fwd_flag", df_trip.store_and_fwd_flag.cast("Boolean"))
df_trip = df_trip.withColumn("PULocationID", df_trip.PULocationID.cast("Integer"))
df_trip = df_trip.withColumn("DOLocationID", df_trip.DOLocationID.cast("Integer"))
df_trip = df_trip.withColumn("payment_type", df_trip.payment_type.cast("Integer"))
df_trip = df_trip.withColumn("fare_amount", df_trip.fare_amount.cast("Double"))
df_trip = df_trip.withColumn("extra", df_trip.extra.cast("Double"))
df_trip = df_trip.withColumn("mta_tax", df_trip.mta_tax.cast("Double"))
df_trip = df_trip.withColumn("tip_amount", df_trip.tip_amount.cast("Double"))
df_trip = df_trip.withColumn("tolls_amount", df_trip.tolls_amount.cast("Double"))
df_trip = df_trip.withColumn("improvement_surcharge", df_trip.improvement_surcharge.cast("Double"))
df_trip = df_trip.withColumn("total_amount", df_trip.total_amount.cast("Double"))
df_trip = df_trip.withColumn("congestion_surcharge", df_trip.congestion_surcharge.cast("Double"))

print('Обновлённая схема yellow_tripdata')
df_trip.printSchema()

df_zone = df_zone.withColumn("LocationID", df_zone.LocationID.cast("Integer"))
print('Обновлённая схема taxi_zone_lookup')
df_zone.printSchema()

# Объединение датафреймов
df = df_trip.join(df_zone, df_trip.PULocationID == df_zone.LocationID)

# Поиск 10-ти районов с наибольшим средним процентом чаевых
df.withColumn("Процент_чаевых", df.tip_amount / df.total_amount) \
    .select(['Borough', 'Процент_чаевых']).groupby('Borough').agg(avg('Процент_чаевых').alias('Средний_процент_чаевых')) \
    .orderBy(desc('Средний_процент_чаевых')).limit(10).show()

# Зависимость среднего расстояния поездки одиночных пассажиров от дня недели
df1 = df.filter(df.passenger_count == 1).withColumn('День_недели', dayofweek(df.tpep_pickup_datetime)) \
    .groupby('День_недели').agg(avg('trip_distance').alias('Среднее_расстояние'))
df1.toPandas().plot(title='Cреднее расстояние поездки одиночных пассажиров по дням недели',
                    x='День_недели', y='Среднее_расстояние', kind='bar', figsize=(8, 4))

# Зависимость средней стоимости поездки одиночных пассажиров от времени суток
df1 = df.filter(df.passenger_count == 1).withColumn('Час_суток', hour(df.tpep_pickup_datetime))
df1 = df1.withColumn('trip_amount', df1.total_amount-df1.tip_amount)
df1 = df1.select('trip_amount', 'Час_суток', when(df1.Час_суток.between(0, 4), 'ночь')
                 .when(df1.Час_суток.between(4, 6), 'раннее утро')
                 .when(df1.Час_суток.between(6, 11), 'утро')
                 .when(df1.Час_суток.between(11, 17), 'день')
                 .when(df1.Час_суток.between(17, 21), 'ранний вечер')
                 .when(df1.Час_суток.between(21, 24), 'поздний вечер').alias('Время_суток')) \
    .groupby('Время_суток').agg(avg('trip_amount').alias('Средняя_стоимость_поездки'))

df1.toPandas().plot(title='Средняя стоимость поездки одиночных пассажиров от времени суток',
                    x='Время_суток', y='Средняя_стоимость_поездки', kind='bar', figsize=(8, 4))

plt.show()
