# pip install kafka-python
# conda install -c conda-forge kafka-python
# https://towardsdatascience.com/kafka-python-explained-in-10-lines-of-code-800e3e07dad1

import kafka
import json

producer = kafka.KafkaProducer(bootstrap_servers=['localhost:9092'],
                               value_serializer=lambda x: json.dumps(x).encode('utf-8'))

for e in range(2):
    data = {'number': e}  # or b'My Python Message
    future = producer.send('test1', value=data)  # test1 is the topic
    result = future.get(timeout=60)
    print(result)

    # or call this to flush the messages
    producer.flush()
