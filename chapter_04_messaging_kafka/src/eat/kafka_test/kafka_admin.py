import kafka.admin as k_admin


admin_client = k_admin.KafkaAdminClient(bootstrap_servers="localhost:9092")

new_topic = k_admin.NewTopic(name="test2", num_partitions=1, replication_factor=1)

admin_client.create_topics(new_topics=[new_topic])

print(admin_client.list_topics())
