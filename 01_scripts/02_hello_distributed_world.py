import getpass
import time

from compas_eve import Message, Publisher, Subscriber, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport


# TODO: create a new class called "HelloPublisher" to be able to print a text on screen on message_published events

# TODO: create a new class called "HelloSubscriber" to be able to handle message_received events


def main():
    # TODO: set the default transport to use `MqttTransport` with the `broker.hivemq.com` host
    # TODO: instantiate the topic using `getpass.getuser()` to get your username

    # TODO: instantiate publisher and subscriber and subscribe

    # TODO: publish multiple messages with a small delay in between

    # TODO: cleanup



if __name__ == "__main__":
    main()
