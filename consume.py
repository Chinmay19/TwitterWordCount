# importing the required modules
from json import loads
from kafka import KafkaConsumer


# generating the Kafka Consumer
tweets_consumer = KafkaConsumer(
    'tweets',
    bootstrap_servers=['localhost:29092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8'))
)

for message in tweets_consumer:  
    message = message.value  
    print(f'new message {message}')