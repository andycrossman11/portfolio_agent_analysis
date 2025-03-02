import pika
import os

ROUTING_KEY = os.environ.get("RABBITMQ_ROUTE", "portfolio_analysis")

def publish_message():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    exchange_name = os.environ.get("RABBITMQ_EXCHANGE", 'portfolio_management')
    channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

    channel.basic_publish(exchange=exchange_name, routing_key=ROUTING_KEY, body='Need a daily portfolio analysis')

    print(f"Sent: message with routing key: '{ROUTING_KEY}'")
    connection.close()

if __name__ == "__main__":
    publish_message('portfolio_analysis', 'Hello, this is an info log!')