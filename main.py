import json
from kafka import KafkaConsumer

topic_name = 'danny-topic'
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')) if m else None,
)


if __name__ == '__main__':
    print(f"Subscribed to topic {topic_name}")

    for message in consumer:
        print(f"{message.value}")
