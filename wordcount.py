# import necessary libraries

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import *

# create sparksession


if __name__ == "__main__":
    print("Usage: wordcount file")

    spark = SparkSession\
        .builder\
        .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1")\
        .config("spark.streaming.stopGracefullyOnShutdown", "true")\
        .appName("PythonWordCount")\
        .getOrCreate()

    spark.sparkContext.setLogLevel('Error')
    

    df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:29092") \
    .option("failOnDataLoss", "false") \
    .option("subscribe", "tweets") \
    .option("startingOffsets", "latest") \
    .load()
    
    sample_df = df.selectExpr("CAST(value as STRING)", "timestamp")
    sample_df.printSchema()
    schema = (
        StructType()
        .add('created_at', StringType())
        .add('id', StringType())
        .add('text', StringType())
    )
    info_df = sample_df.select(
        from_json(col("value"), schema).alias("sample"), 
        "timestamp"
    )
    info_df_final = info_df.select("sample.*", "timestamp")

    word_count_query = info_df_final.withColumn('word', explode(split(col('text'), ' ')))\
        .groupBy('word')\
        .count()\
        .sort('count', ascending=False)\
        .writeStream\
        .format("console")\
        .outputMode("complete")\
        .start()
    
    word_count_query.awaitTermination()


    # def postgres_sink(df, epoch_id):
    #     df.format("jdbc").option("url", "postgresql://localhost:5432/tweets_wordcount")\
    #         .option("dbtable","tweets_count").option("user","tars")\
    #         .option("password", "123QWEasd").save()

    # def process(df, epoch_id):
    #     pass

    # info_df_final.writestream.foreachBatch(process).start()

  

    # query1.awaitTermination()
    # spark.stop()