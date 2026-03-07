from kafka import KafkaConsumer

from config.app_config import AppConfig


if __name__ == '__main__':
    app_config = AppConfig.load_config('dev')
    consumer = KafkaConsumer(
        app_config.consumer_config.topic_name,
        bootstrap_servers=app_config.consumer_config.bootstrap_servers,
        auto_offset_reset=app_config.consumer_config.auto_offset_reset,
        value_deserializer=app_config.consumer_config.value_deserializer,
    )
    print(f"Subscribed to topic {app_config.consumer_config.topic_name}")

    for message in consumer:
        print(f"{message.value}")
