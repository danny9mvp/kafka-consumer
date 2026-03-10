from dataclasses import dataclass


@dataclass
class ConsumerConfig:
    topic_name: str
    bootstrap_servers: str
    auto_offset_reset: str
    value_deserializer: callable
