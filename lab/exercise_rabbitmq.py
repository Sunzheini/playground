"""
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
user: guest, pass: guest
pip install pika
"""
import pika
import threading
import time


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
    def __init__(self) -> None:
        self.connection_parameters = pika.ConnectionParameters('localhost')
        self.connection = None
        self.channel = None
        self.should_stop = False

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

    def stop_consuming(self) -> None:
        """Stop the consumer gracefully."""
        self.should_stop = True
        if self.channel:
            self.channel.stop_consuming()
            print("Consumer stopping...")

    def consume_messages(self, queue_name: str) -> None:
        """Consume messages from the specified queue."""
        if not self.channel:
            raise RuntimeError("Connection not open. Call open_connection() first.")

        def callback(ch, method, properties, body):
            print(f"Received message: {body.decode()}")

        self.channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
        print(f"Waiting for messages in {queue_name}. To exit press CTRL+C")
        self.channel.start_consuming()


def run_producer(queue_name: str = 'letterbox'):
    """Run the producer in a separate thread."""
    producer = RabbitMQProducer()
    producer.open_connection(queue_name=queue_name)

    try:
        # Give consumer time to start
        time.sleep(1)

        # Send messages
        producer.publish_message(message="Hello, RabbitMQ!", queue_name=queue_name)
        time.sleep(0.5)
        producer.publish_message(message="Second message", queue_name=queue_name)
        time.sleep(0.5)
        producer.publish_message(message="Third message", queue_name=queue_name)

        print("Producer finished sending messages")
    finally:
        producer.close_connection()


def run_consumer(queue_name: str = 'letterbox'):
    """Run the consumer in a separate thread."""
    consumer = RabbitMQConsumer()
    consumer.open_connection(queue_name=queue_name)

    try:
        # Start consuming (this will block until stop_consuming is called)
        consumer.consume_messages(queue_name=queue_name)
    except KeyboardInterrupt:
        print("\nConsumer interrupted")
    finally:
        consumer.close_connection()

    return consumer


def run_consumer_wrapper(consumer: RabbitMQConsumer, queue_name: str):
    """Wrapper to run an existing consumer instance in a thread."""
    consumer.open_connection(queue_name=queue_name)

    try:
        consumer.consume_messages(queue_name=queue_name)
    except KeyboardInterrupt:
        print("\nConsumer interrupted")
    finally:
        consumer.close_connection()


if __name__ == "__main__":
    queue_name = 'letterbox'

    # Create consumer instance to control it later
    consumer = RabbitMQConsumer()

    # Create threads for producer and consumer
    consumer_thread = threading.Thread(target=lambda: run_consumer_wrapper(consumer, queue_name))
    producer_thread = threading.Thread(target=run_producer, args=(queue_name,))

    # Start consumer first (it needs to be listening)
    print("Starting consumer thread...")
    consumer_thread.start()

    # Start producer
    print("Starting producer thread...")
    producer_thread.start()

    # Wait for producer to finish
    producer_thread.join()

    # Let consumer run a bit longer to receive all messages
    print("\nWaiting for consumer to process remaining messages...")
    time.sleep(2)

    # Gracefully stop the consumer
    print("Stopping consumer...")
    consumer.stop_consuming()

    # Wait for consumer thread to finish
    consumer_thread.join(timeout=3)

    print("\nAll done!")
