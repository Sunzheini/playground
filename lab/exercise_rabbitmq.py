"""
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
user: guest, pass: guest
pip install pika
"""

import pika


class RabbitMQProducer:
    def __init__(self) -> None:
        self.connection_parameters = pika.ConnectionParameters('localhost')
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='letterbox')

    def publish_message(self, message: str, queue_name: str) -> None:
        """
        Basic publish method to send a message to the 'letterbox' queue using the default exchange.
        :param message: The message to be sent to the queue.
        :param queue_name: The name of the queue to which the message will be sent.
        :return: None
        """
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Message sent: {message}")


class RabbitMQConsumer:
    pass


if __name__ == "__main__":
    producer = RabbitMQProducer()
    consumer = RabbitMQConsumer()

    message = "Hello, RabbitMQ!"
    queue_name = 'letterbox'
    producer.publish_message(message, queue_name)
