#!/usr/bin/python3
from kafka import KafkaConsumer

consumer = KafkaConsumer('demo-topic',
                         api_version=(0,11,5),
                         group_id='my-group',
                         bootstrap_servers=['localhost:29092'])

for message in consumer: 
    print(message)