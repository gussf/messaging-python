#!/usr/bin/python3
from kafka import KafkaProducer
from time import sleep

producer = KafkaProducer(bootstrap_servers='localhost:29092',
                            api_version=(0,11,5),
                            value_serializer=lambda v: str(v).encode('utf-8'))

print("Interrupt with Ctrl+C")
while True:
    ret = producer.send('demo-topic', 'test')
    sleep(0.5)


    