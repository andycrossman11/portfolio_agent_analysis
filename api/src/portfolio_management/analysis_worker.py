import pika
import os
from add_daily_analysis import add_daily_analysis

HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")

def consume_messages(routing_key):
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST))
    channel = connection.channel()

    exchange_name = os.environ.get("RABBITMQ_EXCHANGE", 'portfolio_management')
    queue_name = f'{routing_key}_queue'

    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
    channel.queue_declare(queue=queue_name)
    
    channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

    print(f"Waiting for messages with routing key: {routing_key}")
    channel.basic_consume(queue=queue_name, on_message_callback=add_daily_analysis, auto_ack=True)
    
    channel.start_consuming()

if __name__ == "__main__":
    consume_messages('portfolio_analysis')
