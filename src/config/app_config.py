import json
import yaml
from dataclasses import dataclass, field

from config.consumer_config import ConsumerConfig


@dataclass(frozen=True)
class AppConfig:
    consumer_config: ConsumerConfig = field(default_factory=ConsumerConfig)

    @staticmethod
    def load_config(self, env:str = 'prod'):
        with open(f'src/resources/config-{env}.yaml') as f:
            try:
                config_data = yaml.safe_load(f)
                consumer_config = ConsumerConfig(
                    config_data["consumer-impl"]["consumer"]["topic_name"],
                    config_data["consumer-impl"]["consumer"]["bootstrap_servers"],
                    config_data["consumer-impl"]["consumer"]["auto_offset_reset"],
                    eval(config_data["consumer-impl"]["consumer"]["value_deserializer"]),
                )
                return AppConfig(consumer_config)
            except yaml.YAMLError as exc:
                raise exc
