# https://softwaremill.com/using-kafka-as-a-message-queue/

import kafka


consumer = kafka.KafkaConsumer('test1',
                               bootstrap_servers=['localhost:9092'],
                               auto_offset_reset='earliest',  # read from beginning
                               enable_auto_commit=True,)

for msg in consumer:
    print('msg: ', msg)
    data = msg.value
    print('msg data: ', msg.value)
    # msg.headers are empty, but it's important
