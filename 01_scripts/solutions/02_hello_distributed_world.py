import getpass
import time

from compas_eve import Message, Publisher, Subscriber, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport


class HelloPublisher(Publisher):
    def message_published(self, message):
        print("Published message: " + message.text)


class HelloSubscriber(Subscriber):
    def message_received(self, message):
        print("Received message: " + message.text)


def main():
    host = "broker.hivemq.com"
    set_default_transport(MqttTransport(host=host))

    topic = Topic("/workshop_ds/messages/" + getpass.getuser(), Message)

    publisher = HelloPublisher(topic)
    subscriber = HelloSubscriber(topic)
    subscriber.subscribe()

    for i in range(100):
        publisher.publish(Message(text="Hello World #{}".format(i)))
        time.sleep(1)

    publisher.unadvertise()
    subscriber.unsubscribe()


if __name__ == "__main__":
    main()
