import json
import os
from kafka import KafkaConsumer


BOOTSTRAP_SERVERS = os.getenv('BOOTSTRAP_SERVERS')
TOPIC_NAME = os.getenv('TOPIC_NAME')
consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=BOOTSTRAP_SERVERS,
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) if m else None,
)


if __name__ == '__main__':
    print(f"Subscribed to topic {TOPIC_NAME}")

    for message in consumer:
        print(f"{message.value}")
