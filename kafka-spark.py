import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_json, struct

if __name__ == "__main__":
    # Initialize Spark Session
    spark = SparkSession.builder\
        .appName("Spark connection test")\
        .getOrCreate()
    try:
        kafka_df = spark.read.format("kafka") \
            .option("kafka.bootstrap.servers", "localhost:9092") \
            .option("topic", "invoices")\
            .load()
        kafka_df.printSchema()
        kafka_df.show(5)
    except Exception as e:
        print(f"Failed to connect to Kafka broker: {e}")
    # Read JSON file into DataFrame
    # df = spark.read.json(f".\\data\\invoice.json", multiLine=True)
    # df.show()
    # Kafka expects key-value format, so we need to structure the DataFrame accordingly
    # We use 'None' for the key (or you can specify a filed as key if you need)
    # kafka_df = df.selectExpr("CAST(null AS STRING) as key", "to_json(struct(*)) as value")

    # Write DataFrame to Kafka topic
    # df.write\
    #     .format("setup-env-kafka-1")\
    #     .option("kafka.bootstrap.servers", "localhost:9092")\
    #     .option("topic", "invoices")\
    #     .save()

    # Stop the Spark session
    spark.stop()