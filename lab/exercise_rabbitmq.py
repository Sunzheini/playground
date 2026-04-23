"""
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
user: guest, pass: guest
pip install pika
"""
import pika


class RabbitMQProducer:
    def __init__(self) -> None:
        self.connection_parameters = pika.ConnectionParameters('localhost')
        self.connection = None
        self.channel = None

    def open_connection(self, queue_name: str) -> None:
        """Open connection to RabbitMQ and declare the queue."""
        self.connection = pika.BlockingConnection(self.connection_parameters)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=queue_name)
        print(f"Connection to queue {queue_name} opened")

    def close_connection(self) -> None:
        """Close the connection to RabbitMQ."""
        if self.connection and not self.connection.is_closed:
            self.connection.close()
            print("Connection closed")

    def publish_message(self, message: str, queue_name: str) -> None:
        """
        Basic publish method to send a message to the 'letterbox' queue using the default exchange.
        :param message: The message to be sent to the queue.
        :param queue_name: The name of the queue to which the message will be sent.
        :return: None
        """
        if not self.channel:
            raise RuntimeError("Connection not open. Call open_connection() first.")
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message)
        print(f"Message sent: {message}")


class RabbitMQConsumer:
    pass


if __name__ == "__main__":
    producer = RabbitMQProducer()

    # Open connection
    producer.open_connection(queue_name='letterbox')

    try:
        # Send messages
        message = "Hello, RabbitMQ!"
        queue_name = 'letterbox'
        producer.publish_message(message=message, queue_name=queue_name)

        # You can send more messages here
        producer.publish_message("Second message", queue_name=queue_name)
    finally:
        # Always close the connection
        producer.close_connection()
