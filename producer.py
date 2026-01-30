from confluent_kafka import Producer
import uuid as uui
import json
producer_config={'bootstrap.servers': 'localhost:9092'}
producer=Producer(producer_config)
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered {msg.value().decode('utf-8')} to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
order={'order_id': str(uui.uuid4()),'user':'tarik' ,'item': 'widget', 'quantity': 10}

json.dumps(order).encode('utf-8')
producer.produce(topic='orders', value=json.dumps(order).encode('utf-8'), callback=delivery_report)
producer.flush()