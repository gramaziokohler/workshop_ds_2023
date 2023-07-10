import getpass
import time

from compas_eve import Message, Subscriber, Topic, set_default_transport
from compas_eve.mqtt import MqttTransport


# TODO: create a new class called "ValueSubscriber" to be able to handle message_received events
# each received message will contain `message.value` with the value


def main():
    # TODO: set the default transport to use `MqttTransport` with the `broker.hivemq.com` host
    # TODO: instantiate the topic using `getpass.getuser()` to get your username

    # TODO: instantiate subscriber and subscribe

    # TODO: publish multiple messages with a small delay in between


if __name__ == "__main__":
    main()
